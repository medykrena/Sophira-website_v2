#!/usr/bin/env python3
"""
GÉNÉRATEUR AUTOMATIQUE DE PAGES SOPHIRA
Ce script convertit automatiquement vos anciennes pages HTML vers la nouvelle structure optimisée.
"""

import os
import re
from pathlib import Path

# ============================================
# CONFIGURATION
# ============================================

OLD_SITE_DIR = "Medykrena_website_Sophira-main"  # Dossier de l'ancien site
NEW_SITE_DIR = "sophira-v2"  # Dossier du nouveau site

# Template HTML de base avec la nouvelle structure
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} – Sophira</title>

  <!-- SEO -->
  <link rel="canonical" href="https://sophira.ch{canonical_url}" />
  <meta name="robots" content="index,follow" />
  <meta name="description" content="{description}" />

  <!-- Hreflang -->
  <link rel="alternate" hreflang="fr" href="https://sophira.ch{url_fr}" />
  <link rel="alternate" hreflang="de" href="https://sophira.ch{url_de}" />

  <!-- Favicons -->
  <link rel="icon" href="/assets/icons/favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32x32.png" />

  <!-- CSS -->
  <link rel="stylesheet" href="/assets/css/main.css" />

  <!-- GA4 -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{ dataLayer.push(arguments); }}
    gtag('consent','default',{{
      ad_storage:'denied',
      analytics_storage:'denied',
      functionality_storage:'granted',
      security_storage:'granted',
      ad_user_data:'denied',
      ad_personalization:'denied',
      wait_for_update:500
    }});
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FL1S0MJWB1"></script>
  <script>
    gtag('js', new Date());
    gtag('config', 'G-FL1S0MJWB1');
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Aller au contenu principal</a>

  <div class="overlay">
    <!-- NAVIGATION -->
    <header class="navbar" role="navigation">
      <a class="brand" href="/{lang_dir}/">
        <img src="/assets/images/optimized/logo.webp" alt="Logo Sophira" loading="eager" />
        <h1>Sophira</h1>
      </a>

      <nav class="primary">
        <a href="/{lang_dir}/">Accueil</a>
        <a href="/{lang_dir}/team.html">Équipe</a>
        <a href="/{lang_dir}/project.html">Projet social</a>
        <a href="/{lang_dir}/dashboard.html">Tableau de bord</a>
        <a href="/jobs/">Portail Emplois</a>
        <a href="/{lang_dir}/blog.html">Blog</a>
        <a href="/{lang_dir}/contact.html">Contact</a>
      </nav>

      <div class="controls">
        <button class="lang-btn" id="lang-btn" aria-haspopup="true" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <circle cx="12" cy="12" r="10" stroke-width="2"/>
            <path d="M2 12h20M12 2a15.3 15.3 0 010 20M12 2a15.3 15.3 0 000 20" stroke-width="2" stroke-linecap="round"/>
          </svg>
          {lang_upper}
        </button>
        <div id="lang-menu" class="lang-menu" aria-hidden="true">
          <a href="{url_fr}" lang="fr" {current_fr}>Français</a>
          <a href="{url_de}" lang="de" {current_de}>Deutsch</a>
        </div>

        <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-controls="menu-mobile" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M3 6h18M3 12h18M3 18h18" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
    </header>

    <div id="menu-mobile" class="mobile-panel" hidden>
      <div class="mobile-links">
        <a href="/{lang_dir}/">Accueil</a>
        <a href="/{lang_dir}/team.html">Équipe</a>
        <a href="/{lang_dir}/project.html">Projet social</a>
        <a href="/{lang_dir}/dashboard.html">Tableau de bord</a>
        <a href="/jobs/">Portail Emplois</a>
        <a href="/{lang_dir}/blog.html">Blog</a>
        <a href="/{lang_dir}/contact.html">Contact</a>
      </div>
    </div>

    <!-- MAIN CONTENT -->
    <main id="main" class="container">
{content}
    </main>

    <footer>
      <p>&copy; 2026 Sophira Association | Basel, Suisse | 
         <a href="/{lang_dir}/privacy.html">Confidentialité</a> | 
         <a href="/{lang_dir}/legal.html">Mentions légales</a>
      </p>
    </footer>
  </div>

  <a class="chat-fab" href="https://chatgpt.com/g/g-68d273dcee0081918dc19a72db072503-sophira-ai-assistant" target="_blank" rel="noopener">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
      <path d="M21 15a4 4 0 0 1-4 4H8l-5 4V7a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4v8z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <span>Assistant Sophira</span>
  </a>

  <div id="cookie-banner" class="cookie-banner" role="dialog">
    <p><strong>Cookies & confidentialité.</strong> Nous utilisons des cookies essentiels au fonctionnement du site et, avec votre accord, des mesures d'audience (Google Analytics). <a href="/{lang_dir}/privacy.html">En savoir plus</a></p>
    <div class="cookie-actions">
      <button class="btn minor" id="cookie-refuse">Refuser l'analyse</button>
      <button class="btn" id="cookie-accept">Accepter l'analyse</button>
      <button class="btn outline" id="cookie-later">Plus tard</button>
    </div>
  </div>

  <script src="/assets/js/main.js"></script>
</body>
</html>'''

# ============================================
# FONCTIONS
# ============================================

def extract_content(html_content):
    """Extrait le contenu principal d'un fichier HTML"""
    # Chercher le contenu entre <main> et </main>
    match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
    if match:
        content = match.group(1)
        # Nettoyer les attributs id="main" etc
        content = re.sub(r'id="main"', '', content)
        content = re.sub(r'class="container"', '', content)
        return content.strip()
    
    # Si pas de <main>, chercher entre <!-- CONTENU --> et <footer>
    match = re.search(r'<!-- CONTENU -->(.*?)<footer', html_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    return "<section class='content'><h1>Contenu à ajouter</h1><p>Cette page doit être complétée manuellement.</p></section>"

def extract_title(html_content):
    """Extrait le titre de la page"""
    match = re.search(r'<title>(.*?)</title>', html_content)
    if match:
        title = match.group(1)
        # Retirer " – Sophira" si présent
        title = title.replace(' – Sophira', '').replace(' - Sophira', '')
        return title
    return "Page"

def extract_description(html_content):
    """Extrait la meta description"""
    match = re.search(r'<meta name="description" content="(.*?)"', html_content)
    if match:
        return match.group(1)
    return "Sophira Association - Reconversion professionnelle en Suisse"

def update_image_paths(content):
    """Met à jour les chemins d'images vers la nouvelle structure"""
    # Remplacer les chemins d'images
    content = re.sub(r'src="Logo_sophira\.png"', 'src="/assets/images/optimized/logo.webp"', content)
    content = re.sub(r'src="mathew-schwartz.*?\.jpg"', 'src="/assets/images/optimized/background.webp"', content)
    content = re.sub(r'src="PHOTO-BAO\.jpg"', 'src="/assets/images/optimized/photo-bao.webp"', content)
    content = re.sub(r'src="img_1\.jpg"', 'src="/assets/images/optimized/img-1.webp"', content)
    content = re.sub(r'src="twint_QR\.png"', 'src="/assets/images/optimized/twint-qr.webp"', content)
    return content

def update_links(content, is_de=False):
    """Met à jour les liens internes vers la nouvelle structure"""
    lang_dir = "de" if is_de else "fr"
    
    # Liens vers pages simples
    content = re.sub(r'href="index\.html"', f'href="/{lang_dir}/"', content)
    content = re.sub(r'href="project\.html"', f'href="/{lang_dir}/project.html"', content)
    content = re.sub(r'href="team\.html"', f'href="/{lang_dir}/team.html"', content)
    content = re.sub(r'href="blog\.html"', f'href="/{lang_dir}/blog.html"', content)
    content = re.sub(r'href="contact\.html"', f'href="/{lang_dir}/contact.html"', content)
    content = re.sub(r'href="donate\.html"', f'href="/{lang_dir}/donate.html"', content)
    content = re.sub(r'href="privacy\.html"', f'href="/{lang_dir}/privacy.html"', content)
    content = re.sub(r'href="mentions\.html"', f'href="/{lang_dir}/legal.html"', content)
    content = re.sub(r'href="dashboard\.html"', f'href="/{lang_dir}/dashboard.html"', content)
    
    # Liens vers versions -de
    if not is_de:
        content = re.sub(r'href="index-de\.html"', 'href="/de/"', content)
        content = re.sub(r'href="(\w+)-de\.html"', r'href="/de/\1.html"', content)
    
    # Articles blog
    content = re.sub(r'href="article(\d+)\.html"', rf'href="/blog/{lang_dir}/article-\1.html"', content)
    
    # Jobs portal
    content = re.sub(r'href="jobs/index\.html"', 'href="/jobs/"', content)
    
    return content

def generate_page(old_file, new_file, lang='fr'):
    """Génère une nouvelle page à partir d'une ancienne"""
    
    print(f"  📄 Génération: {new_file}")
    
    # Lire l'ancien fichier
    try:
        with open(old_file, 'r', encoding='utf-8') as f:
            old_content = f.read()
    except FileNotFoundError:
        print(f"    ⚠️ Fichier source non trouvé: {old_file}")
        return False
    
    # Extraire les informations
    title = extract_title(old_content)
    description = extract_description(old_content)
    content = extract_content(old_content)
    
    # Mettre à jour les chemins
    content = update_image_paths(content)
    content = update_links(content, is_de=(lang=='de'))
    
    # Déterminer les URLs
    page_name = Path(new_file).stem
    if page_name == 'index':
        url_fr = "/fr/"
        url_de = "/de/"
    else:
        url_fr = f"/fr/{page_name}.html"
        url_de = f"/de/{page_name}.html"
    
    canonical_url = url_fr if lang == 'fr' else url_de
    lang_dir = "fr" if lang == "fr" else "de"
    lang_upper = "FR" if lang == "fr" else "DE"
    current_fr = 'aria-current="true"' if lang == "fr" else ''
    current_de = 'aria-current="true"' if lang == "de" else ''
    
    # Générer le HTML final
    html = HTML_TEMPLATE.format(
        lang=lang,
        title=title,
        canonical_url=canonical_url,
        description=description,
        url_fr=url_fr,
        url_de=url_de,
        lang_dir=lang_dir,
        lang_upper=lang_upper,
        current_fr=current_fr,
        current_de=current_de,
        content=content
    )
    
    # Créer le dossier si nécessaire
    os.makedirs(os.path.dirname(new_file), exist_ok=True)
    
    # Écrire le nouveau fichier
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"    ✅ Créé!")
    return True

# ============================================
# LISTE DES PAGES À GÉNÉRER
# ============================================

PAGES_TO_GENERATE = [
    # Pages FR
    ('project.html', 'sophira-v2/fr/project.html', 'fr'),
    ('team.html', 'sophira-v2/fr/team.html', 'fr'),
    ('blog.html', 'sophira-v2/fr/blog.html', 'fr'),
    ('contact.html', 'sophira-v2/fr/contact.html', 'fr'),
    ('donate.html', 'sophira-v2/fr/donate.html', 'fr'),
    ('mentions.html', 'sophira-v2/fr/legal.html', 'fr'),
    ('dashboard.html', 'sophira-v2/fr/dashboard.html', 'fr'),
    
    # Pages DE
    ('project-de.html', 'sophira-v2/de/index.html', 'de'),
    ('project-de.html', 'sophira-v2/de/project.html', 'de'),
    ('team-de.html', 'sophira-v2/de/team.html', 'de'),
    ('blog-de.html', 'sophira-v2/de/blog.html', 'de'),
    ('contact-de.html', 'sophira-v2/de/contact.html', 'de'),
    ('donate-de.html', 'sophira-v2/de/donate.html', 'de'),
    ('mentions-de.html', 'sophira-v2/de/legal.html', 'de'),
    ('dashboard-de.html', 'sophira-v2/de/dashboard.html', 'de'),
    ('privacy-de.html', 'sophira-v2/de/privacy.html', 'de'),
    
    # Articles FR
    ('article1.html', 'sophira-v2/blog/fr/article-1.html', 'fr'),
    ('article2.html', 'sophira-v2/blog/fr/article-2.html', 'fr'),
    ('article3.html', 'sophira-v2/blog/fr/article-3.html', 'fr'),
    ('article4.html', 'sophira-v2/blog/fr/article-4.html', 'fr'),
    ('article5.html', 'sophira-v2/blog/fr/article-5.html', 'fr'),
    ('article6.html', 'sophira-v2/blog/fr/article-6.html', 'fr'),
    ('article7.html', 'sophira-v2/blog/fr/article-7.html', 'fr'),
]

# ============================================
# MAIN
# ============================================

def main():
    print("=" * 60)
    print("🚀 GÉNÉRATEUR AUTOMATIQUE SOPHIRA")
    print("=" * 60)
    print()
    
    total = len(PAGES_TO_GENERATE)
    success = 0
    failed = 0
    
    for old_filename, new_filepath, lang in PAGES_TO_GENERATE:
        old_filepath = os.path.join(OLD_SITE_DIR, old_filename)
        
        if generate_page(old_filepath, new_filepath, lang):
            success += 1
        else:
            failed += 1
    
    print()
    print("=" * 60)
    print("📊 RÉSUMÉ")
    print("=" * 60)
    print(f"✅ Pages créées avec succès: {success}/{total}")
    if failed > 0:
        print(f"⚠️ Pages échouées: {failed}/{total}")
    print()
    print("🎉 Génération terminée!")
    print()
    print("📝 PROCHAINES ÉTAPES:")
    print("1. Vérifier les pages générées dans sophira-v2/")
    print("2. Ajuster manuellement si nécessaire")
    print("3. Télécharger les fonts Inter (voir assets/fonts/README_FONTS.md)")
    print("4. Uploader sur GitHub")
    print("5. Déployer sur Netlify")
    print()

if __name__ == "__main__":
    main()
