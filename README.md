# 🌟 SOPHIRA.CH - SITE WEB V2

**Version 2.0** - Site vitrine bilingue (FR/DE) pour l'association Sophira  
**Déploiement :** Netlify → `sophira.ch`  
**Repository :** `Sophira-website_v2`

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#-vue-densemble)
2. [Structure du projet](#-structure-du-projet)
3. [Technologies utilisées](#-technologies-utilisées)
4. [Configuration Netlify](#-configuration-netlify)
5. [SEO et indexation Google](#-seo-et-indexation-google)
6. [Performance](#-performance)
7. [Sécurité](#-sécurité)
8. [Déploiement](#-déploiement)
9. [Troubleshooting](#-troubleshooting)
10. [Maintenance](#-maintenance)
11. [Historique des problèmes résolus](#-historique-des-problèmes-résolus)

---

## 🎯 VUE D'ENSEMBLE

### Qu'est-ce que Sophira ?

**Sophira** est une association suisse à but non lucratif basée à Bâle qui accompagne les adultes en difficulté financière dans leur reconversion professionnelle vers les métiers du numérique (data, IA, technologies vertes).

### Architecture du site

- **Site vitrine bilingue** : `/fr/` (français) et `/de/` (allemand)
- **Blog** : Articles FR/DE dans `/blog/fr/` et `/blog/de/`
- **Portail emplois** : Section séparée `/jobs/`
- **Hébergement** : Netlify avec domaine personnalisé `sophira.ch`

### Amélirations V2 vs V1

| Aspect | V1 (Ancien) | V2 (Actuel) | Gain |
|--------|-------------|-------------|------|
| **Taille page accueil** | ~2.8 MB | ~400 KB | **-85%** |
| **Fichiers CSS** | 24 inline | 1 externe consolidé | **-96%** |
| **Images** | PNG/JPG lourds | WebP optimisés | **-62%** |
| **Structure URL** | Incohérente (`-de.html`) | Propre (`/de/`) | ✅ |
| **Redirections** | Multiples conditionnelles | 301 simples | ✅ |
| **SEO** | Basique | Optimisé (hreflang, sitemap) | ✅ |
| **Sécurité** | Headers basiques | CSP complet + HSTS | ✅ |
| **Fonts** | CDN Google Fonts | Self-hosted | ✅ |
| **Favicons** | 0/4 formats | 4/4 formats | ✅ |

---

## 📁 STRUCTURE DU PROJET

```
Sophira-website_v2/
│
├── fr/                          # Site vitrine français
│   ├── index.html              # Page d'accueil FR ✅
│   ├── project.html            # Le projet social
│   ├── team.html               # L'équipe
│   ├── blog.html               # Index blog FR
│   ├── dashboard.html          # Tableaux de bord (Tableau Public)
│   ├── contact.html            # Formulaire contact
│   ├── donate.html             # Page dons (Twint QR)
│   ├── privacy.html            # Confidentialité (LPD suisse)
│   └── legal.html              # Mentions légales
│
├── de/                          # Site vitrine allemand
│   ├── index.html              # Page d'accueil DE ✅
│   └── (même structure que FR)
│
├── blog/
│   ├── fr/
│   │   ├── article-1.html      # Article 1 FR
│   │   ├── article-2.html      # Article 2 FR
│   │   └── ...                 # 7 articles total
│   └── de/
│       └── (articles DE - à créer)
│
├── jobs/                        # Portail emplois (séparé)
│   ├── index.html              # Liste des offres
│   └── apply.html              # Formulaire candidature
│
├── assets/
│   ├── css/
│   │   └── main.css            # CSS consolidé unique ✅
│   ├── js/
│   │   └── main.js             # JavaScript modulaire ✅
│   ├── fonts/
│   │   ├── inter-400.woff2     # Font Regular
│   │   ├── inter-600.woff2     # Font SemiBold
│   │   └── README_FONTS.md     # Instructions téléchargement
│   ├── images/
│   │   ├── optimized/          # Images WebP optimisées
│   │   │   ├── logo.webp
│   │   │   ├── background.webp
│   │   │   ├── photo-bao.webp
│   │   │   └── img-1.webp
│   │   └── fallback/           # Images originales (backup)
│   │       ├── Logo_sophira.png
│   │       └── mathew-schwartz-*.jpg
│   └── icons/                  # Favicons
│       ├── favicon.ico         # 16x16 + 32x32 multi-taille
│       ├── favicon-16x16.png
│       ├── favicon-32x32.png
│       └── apple-touch-icon.png # 180x180 iOS
│
├── docs/                        # Documentation et scripts
│   ├── generate_page.py        # Script migration V1→V2
│   └── README_MIGRATION.md     # Documentation migration
│
├── netlify.toml                # Configuration Netlify ✅
├── robots.txt                  # Directives crawlers ✅
├── sitemap.xml                 # Plan du site (27 URLs) ✅
├── 404.html                    # Page erreur 404 ✅
└── README.md                   # Ce fichier

**⚠️ FICHIERS SUPPRIMÉS (ne pas recréer) :**
- ❌ `/index.html` à la racine (causait redirect error Google)
  → La redirection est gérée par `netlify.toml` uniquement

**⚠️ FICHIERS PHOTOS À LA RACINE (temporaire) :**
- `/photoCV.png` : Photo Arijanit (Président)
- `/photoURS.png` : Photo Urs (Trésorier) - **À UPLOADER**

**Recommandation :** Déplacer vers `/assets/images/team/` et mettre à jour HTML
```

---

## 🛠 TECHNOLOGIES UTILISÉES

### Frontend
- **HTML5** : Sémantique, accessible (ARIA labels)
- **CSS3** : Variables CSS, Grid, Flexbox, responsive mobile-first
- **JavaScript Vanilla** : Pas de frameworks, code modulaire
- **WebP** : Format d'image moderne (-62% poids vs PNG/JPG)

### Fonts
- **Inter** (Google Fonts) : Self-hosted pour performance et RGPD
  - `inter-400.woff2` : Regular (texte courant)
  - `inter-600.woff2` : SemiBold (titres, boutons)
  
**⚠️ NOTE :** Bien que dans le CSS on référence encore `https://fonts.googleapis.com`, les fonts sont **réellement chargées depuis `/assets/fonts/`** via `@font-face`. Les références Google Fonts dans le CSP sont pour compatibilité uniquement.

### Hébergement et déploiement
- **Netlify** : Hébergement JAMstack avec CI/CD
- **GitHub** : Repository principal
- **Domaine** : `sophira.ch` (configuré sur Netlify)

### Analytics et tracking
- **Google Analytics 4** (GA4) : `G-FL1S0MJWB1`
- **Consent Mode v2** : Conformité RGPD/LPD
- **Cookie banner** : Gestion consentement utilisateur

### Intégrations tierces
- **Tableau Public** : 7 dashboards embarqués (iframes)
- **ChatGPT Custom GPT** : Assistant Sophira (bouton flottant)
- **Twint** : QR code pour dons (page `/donate.html`)

---

## ⚙️ CONFIGURATION NETLIFY

### Fichier `netlify.toml`

**Emplacement :** Racine du repository  
**Rôle :** Configure redirections, headers de sécurité, cache

#### Redirections 301 (SEO)

```toml
# Redirection racine simple (pas de conditions langue)
[[redirects]]
  from = "/"
  to = "/fr/"
  status = 301
  force = false

# Migration pages anciennes → nouvelles
[[redirects]]
  from = "/index.html"
  to = "/fr/"
  status = 301

# Articles blog
[[redirects]]
  from = "/article1.html"
  to = "/blog/fr/article-1.html"
  status = 301
```

**⚠️ IMPORTANT :** 
- **Une seule redirection `/` vers `/fr/`** (pas de conditions `{Language = ["fr"]}`)
- **Status 301** (permanent) pour préserver le ranking SEO
- **Pas de `/index.html` à la racine** du repo (conflit redirection)

#### Headers de sécurité

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Strict-Transport-Security = "max-age=31536000; includeSubDomains; preload"
    
    Content-Security-Policy = '''
      default-src 'self';
      script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://public.tableau.com;
      frame-src https://chatgpt.com https://public.tableau.com;
      ...
    '''
```

**⚠️ CSP pour Tableau Public :**
- `frame-src` doit inclure `https://public.tableau.com`
- `script-src` doit inclure `https://public.tableau.com`
- Sans ces règles, les iframes Tableau ne s'affichent pas

#### Headers de cache

```toml
# Cache agressif assets (1 an)
[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

# Pas de cache HTML (toujours à jour)
[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"
```

### Domaine personnalisé

**Domaine principal :** `sophira.ch`  
**Site Netlify :** `sophira-verein`  
**URL Netlify :** `sophira-verein.netlify.app`

**Configuration :**
1. Netlify Dashboard → Site settings → Domain management
2. Add custom domain → `sophira.ch`
3. DNS automatiquement configuré par Netlify
4. HTTPS/SSL géré automatiquement (Let's Encrypt)

**Autres sites sur le compte Netlify :**
- `sophira` → `sophira.netlify.app` (ancien site, à désactiver)
- `drone-academy` → `drone-academy.ch` (projet séparé)

---

## 🔍 SEO ET INDEXATION GOOGLE

### Balises meta essentielles

**Dans chaque page HTML :**

```html
<head>
  <!-- SEO de base -->
  <title>Titre de la page – Sophira</title>
  <meta name="description" content="Description 150-160 caractères" />
  <link rel="canonical" href="https://sophira.ch/fr/page.html" />
  <meta name="robots" content="index,follow" />
  
  <!-- Hreflang (multilingue) -->
  <link rel="alternate" hreflang="fr" href="https://sophira.ch/fr/page.html" />
  <link rel="alternate" hreflang="de" href="https://sophira.ch/de/page.html" />
  <link rel="alternate" hreflang="x-default" href="https://sophira.ch/fr/page.html" />
  
  <!-- Open Graph (réseaux sociaux) -->
  <meta property="og:title" content="Titre de la page" />
  <meta property="og:description" content="Description" />
  <meta property="og:url" content="https://sophira.ch/fr/page.html" />
  <meta property="og:image" content="https://sophira.ch/assets/images/optimized/logo.webp" />
</head>
```

### Fichier `robots.txt`

**Emplacement :** Racine du repository  
**URL :** `https://sophira.ch/robots.txt`

```txt
User-agent: *
Allow: /

# Autoriser explicitement les assets (JS, CSS, images)
Allow: /assets/

# Bloquer uniquement fichiers de configuration
Disallow: /_headers
Disallow: /netlify.toml

# Bloquer paramètres de tracking
Disallow: /*?utm_*
Disallow: /*?fbclid=*

# Sitemap
Sitemap: https://sophira.ch/sitemap.xml
```

**⚠️ ERREUR FRÉQUENTE :**
```txt
# ❌ NE JAMAIS FAIRE CECI (bloque le JavaScript)
Disallow: /assets/js/
```

**Conséquence :** Google ne peut pas charger `main.js` → Page considérée comme cassée

### Fichier `sitemap.xml`

**Emplacement :** Racine du repository  
**URL :** `https://sophira.ch/sitemap.xml`  
**Pages indexées :** 27 URLs

**Détail des 27 URLs :**
- 2 × Pages d'accueil (`/fr/`, `/de/`)
- 2 × Project (`/fr/project.html`, `/de/project.html`)
- 2 × Team (`/fr/team.html`, `/de/team.html`)
- 2 × Dashboard (`/fr/dashboard.html`, `/de/dashboard.html`) **← Ajoutés en mars 2026**
- 2 × Blog index (`/fr/blog.html`, `/de/blog.html`)
- 2 × Contact (`/fr/contact.html`, `/de/contact.html`)
- 2 × Donate (`/fr/donate.html`, `/de/donate.html`)
- 2 × Privacy (`/fr/privacy.html`, `/de/privacy.html`)
- 2 × Legal (`/fr/legal.html`, `/de/legal.html`)
- 7 × Articles blog FR (`/blog/fr/article-1.html` à `article-7.html`)
- 1 × Jobs portal (`/jobs/`)
- **Total : 27 URLs**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  
  <!-- Page d'accueil FR -->
  <url>
    <loc>https://sophira.ch/fr/</loc>
    <lastmod>2026-03-08</lastmod>
    <xhtml:link rel="alternate" hreflang="fr" href="https://sophira.ch/fr/" />
    <xhtml:link rel="alternate" hreflang="de" href="https://sophira.ch/de/" />
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- ... autres pages ... -->
</urlset>
```

**Soumission à Google :**
1. Google Search Console → Sitemaps
2. Ajouter sitemap : `https://sophira.ch/sitemap.xml`
3. Vérifier que toutes les URLs sont découvertes

### Google Search Console

**Propriété :** `https://sophira.ch`  
**Vérification :** Balise meta HTML (déjà configurée)

**Commandes importantes :**
1. **URL Inspection** : Tester une URL spécifique
2. **Test Live URL** : Voir comment Google crawle en temps réel
3. **Request Indexing** : Forcer l'indexation d'une page

**Vérification des ressources :**
- CSS : `https://sophira.ch/assets/css/main.css` ✅
- JS : `https://sophira.ch/assets/js/main.js` ✅
- Fonts : `inter-400.woff2`, `inter-600.woff2` ✅
- Images : `logo.webp`, `background.webp` ✅

**Si "Page resources: 7/8 loaded" :**
→ Vérifier `robots.txt` (problème fréquent : `/assets/js/` bloqué)

---

## ⚡ PERFORMANCE

### Optimisations images

**Conversion PNG/JPG → WebP :**

| Image | Format original | Taille avant | Format optimisé | Taille après | Gain |
|-------|----------------|--------------|-----------------|--------------|------|
| Background | JPG | 2.6 MB | WebP | 980 KB | **-62%** |
| Logo | PNG | 450 KB | WebP | 85 KB | **-81%** |
| Photo Bao | JPG | 1.2 MB | WebP | 320 KB | **-73%** |

**Attributs d'images optimisés :**
```html
<img 
  src="/assets/images/optimized/logo.webp" 
  alt="Logo Sophira" 
  width="200" 
  height="80"
  loading="lazy"        <!-- Lazy loading -->
  decoding="async"      <!-- Décodage asynchrone -->
  fetchpriority="high"  <!-- Priorité élevée (hero image seulement) -->
/>
```

### Consolidation CSS/JS

**Avant (V1) :**
- 24 fichiers CSS inline (`<style>` dans chaque HTML)
- JavaScript éparpillé dans les pages

**Après (V2) :**
- 1 seul fichier CSS externe : `/assets/css/main.css` (mis en cache)
- 1 seul fichier JS externe : `/assets/js/main.js` (mis en cache)

**Avantages :**
- ✅ Cache navigateur (pas de re-téléchargement)
- ✅ Maintenance simplifiée (1 fichier à modifier)
- ✅ Taille totale réduite (pas de duplication)

### Fonts self-hosted

**Avant (V1) :** Google Fonts CDN
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
```

**Après (V2) :** Self-hosted
```css
@font-face {
  font-family: 'Inter';
  src: url('/assets/fonts/inter-400.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
```

**Avantages :**
- ✅ Pas de requête DNS externe (plus rapide)
- ✅ Conformité RGPD/LPD (pas de transfert vers Google)
- ✅ Contrôle total sur les versions

### Scores de performance

**Target :**
- **Lighthouse Performance** : 90+
- **First Contentful Paint (FCP)** : < 1.5s
- **Largest Contentful Paint (LCP)** : < 2.5s
- **Cumulative Layout Shift (CLS)** : < 0.1

---

## 🔒 SÉCURITÉ

### Content Security Policy (CSP)

**Configuré dans `netlify.toml` :**

```toml
Content-Security-Policy = '''
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://public.tableau.com;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com;
  img-src 'self' data: https:;
  connect-src 'self' https://www.google-analytics.com;
  frame-src https://chatgpt.com https://public.tableau.com;
  base-uri 'self';
  form-action 'self';
  upgrade-insecure-requests;
'''
```

**Explications :**
- `default-src 'self'` : Par défaut, seules ressources du même domaine
- `script-src` : Scripts autorisés (GA4 + Tableau + inline)
- `frame-src` : Iframes autorisées (ChatGPT GPT + Tableau)
- `upgrade-insecure-requests` : Force HTTPS automatiquement

**⚠️ Erreurs fréquentes :**
1. **Oublier `https://public.tableau.com` dans `frame-src`**  
   → Les dashboards Tableau ne s'affichent pas
2. **Oublier `'unsafe-inline'` dans `script-src`**  
   → Google Analytics ne fonctionne pas

### HSTS (HTTP Strict Transport Security)

```toml
Strict-Transport-Security = "max-age=31536000; includeSubDomains; preload"
```

**Signification :**
- Force HTTPS pendant 1 an (`max-age=31536000`)
- S'applique aux sous-domaines (`includeSubDomains`)
- Éligible à la liste de preload navigateurs (`preload`)

### Autres headers de sécurité

```toml
X-Frame-Options = "DENY"              # Pas d'iframe du site ailleurs
X-Content-Type-Options = "nosniff"    # Pas de sniffing MIME
X-XSS-Protection = "1; mode=block"    # Protection XSS
Referrer-Policy = "strict-origin-when-cross-origin"
```

### Permissions-Policy

```toml
Permissions-Policy = '''
  geolocation=(),
  microphone=(),
  camera=(),
  payment=(),
  usb=()
'''
```

**Désactive les APIs sensibles** (géolocalisation, micro, caméra, etc.)

---

## 🚀 DÉPLOIEMENT

### Prérequis

1. **Compte GitHub** : Repository `Sophira-website_v2`
2. **Compte Netlify** : Lié au GitHub
3. **Fonts Inter téléchargées** : Voir `/assets/fonts/README_FONTS.md`

### Étapes de déploiement

#### 1. Préparer le repository local

```bash
# Cloner ou télécharger le code
git clone https://github.com/medykrena/Sophira-website_v2.git
cd Sophira-website_v2

# Vérifier la structure
ls -la
# Doit contenir : fr/ de/ assets/ netlify.toml robots.txt sitemap.xml
```

#### 2. Télécharger les fonts (si pas déjà fait)

```bash
cd assets/fonts/

# Télécharger Inter depuis Google Fonts
# https://fonts.google.com/specimen/Inter
# Sélectionner poids : 400 (Regular) et 600 (SemiBold)
# Télécharger les fichiers .woff2

# Placer les fichiers :
# - inter-400.woff2
# - inter-600.woff2
```

#### 3. Push vers GitHub

```bash
git add .
git commit -m "Deploy: Site Sophira V2 optimisé"
git push origin main
```

#### 4. Déployer sur Netlify

**Option A : Déploiement automatique (recommandé)**

1. Netlify Dashboard → Sites
2. Le site `sophira-verein` se déploie automatiquement
3. Attendre ~1-2 minutes
4. Vérifier le déploiement dans "Deploys"

**Option B : Déploiement manuel**

1. Netlify Dashboard → Sites → `sophira-verein`
2. Deploys → Trigger deploy → Deploy site
3. Attendre la fin du build

#### 5. Vérifier le déploiement

**Checklist post-déploiement :**

- [ ] Site accessible sur `https://sophira.ch`
- [ ] Pages FR accessibles (`/fr/`, `/fr/project.html`, etc.)
- [ ] Pages DE accessibles (`/de/`, `/de/project.html`, etc.)
- [ ] Images chargées correctement (WebP)
- [ ] Fonts chargées (Inter 400 et 600)
- [ ] CSS appliqué (couleurs, layout)
- [ ] JavaScript fonctionnel (menu mobile, cookies, langue)
- [ ] Formulaires opérationnels (contact, newsletter)
- [ ] Dashboards Tableau visibles (page dashboard)
- [ ] Bouton ChatGPT GPT fonctionnel
- [ ] Google Analytics actif (vérifier GA4 Real-time)
- [ ] Redirections 301 fonctionnelles (tester anciennes URLs)
- [ ] HTTPS actif (cadenas vert)
- [ ] 404.html s'affiche sur page inexistante

#### 6. Tests Google Search Console

1. Google Search Console → URL Inspection
2. Tester `https://sophira.ch/`
3. Cliquer "Test Live URL"
4. Vérifier "Page resources: All resources were loaded"
5. Cliquer "Request Indexing"

---

## 🐛 TROUBLESHOOTING

### Problème : Google "Redirect error"

**Symptôme :**
```
Page fetch: Failed: Redirect error
Page is not indexed: Redirect error
```

**Causes possibles :**

1. **Redirections conditionnelles dans `netlify.toml`**
```toml
# ❌ MAUVAIS (cause le problème)
[[redirects]]
  from = "/"
  to = "/fr/"
  conditions = {Language = ["fr"]}
```

**Solution :** Une seule redirection simple 301
```toml
# ✅ BON
[[redirects]]
  from = "/"
  to = "/fr/"
  status = 301
  force = false
```

2. **Fichier `/index.html` à la racine**

Si vous avez un fichier `/index.html` avec meta refresh ou JS redirect :
```html
<!-- ❌ SUPPRIMEZ CE FICHIER -->
<meta http-equiv="refresh" content="0; url=/fr/">
```

**Solution :** Supprimer complètement `/index.html` à la racine

### Problème : "Googlebot blocked by robots.txt"

**Symptôme :**
```
Page resources: 7/8 loaded
Script: https://sophira.ch/assets/js/main.js - Blocked by robots.txt
```

**Cause :** `robots.txt` bloque `/assets/js/`

```txt
# ❌ MAUVAIS
Disallow: /assets/js/
```

**Solution :** Autoriser `/assets/`
```txt
# ✅ BON
Allow: /assets/
```

### Problème : Dashboards Tableau ne s'affichent pas

**Symptôme :** Cadre vide ou erreur console CSP

**Cause :** CSP bloque `https://public.tableau.com`

**Solution :** Vérifier `netlify.toml`
```toml
Content-Security-Policy = '''
  frame-src https://public.tableau.com;  ← Doit être présent
  script-src 'self' https://public.tableau.com;  ← Doit être présent
'''
```

**Format iframe correct :**
```html
<iframe 
  src="https://public.tableau.com/views/VizName/Dashboard?:showVizHome=no&embed=true"
  title="Dashboard title"
  loading="lazy">
</iframe>
```

**⚠️ Paramètres URL importants :**
- `?:showVizHome=no&embed=true` ✅ (fonctionne)
- `?:embed=yes&:toolbar=yes` ❌ (ne fonctionne pas)

### Problème : Fonts ne se chargent pas

**Symptôme :** Texte en fallback (Arial/system fonts)

**Causes possibles :**

1. **Fichiers .woff2 manquants**
```bash
# Vérifier présence
ls assets/fonts/
# Doit contenir : inter-400.woff2 et inter-600.woff2
```

2. **Chemins CSS incorrects**
```css
/* ❌ MAUVAIS */
src: url('./fonts/inter-400.woff2');

/* ✅ BON */
src: url('/assets/fonts/inter-400.woff2');
```

3. **CORS bloqué**

Vérifier `netlify.toml` :
```toml
[[headers]]
  for = "/assets/fonts/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
    Access-Control-Allow-Origin = "*"  ← Doit être présent
```

### Problème : Images WebP ne s'affichent pas

**Cause 1 : Navigateur ancien** (Safari < 14, IE)

**Solution :** Ajouter fallback
```html
<picture>
  <source srcset="/assets/images/optimized/logo.webp" type="image/webp">
  <img src="/assets/images/fallback/Logo_sophira.png" alt="Logo Sophira">
</picture>
```

**Cause 2 : Fichiers manquants**

Vérifier présence :
```bash
ls assets/images/optimized/
# Doit contenir : logo.webp, background.webp, photo-bao.webp, img-1.webp
```

### Problème : Page 404 personnalisée ne s'affiche pas

**Symptôme :** Page 404 Netlify par défaut au lieu de `/404.html`

**Solution :** Vérifier que `404.html` est à la **racine** du repo
```
Sophira-website_v2/
├── 404.html  ← ICI (pas dans /fr/ ou /de/)
├── fr/
└── de/
```

**⚠️ IMPORTANT :** 
- ✅ **GARDER** `/404.html` (page d'erreur personnalisée utilisée par Netlify)
- ❌ **NE PAS** créer `/index.html` à la racine (causait redirect error Google)

**Différence :**
- `/404.html` = Affichée automatiquement quand page introuvable ✅
- `/index.html` = Entre en conflit avec redirections `netlify.toml` ❌

### Problème : Google Analytics ne track pas

**Vérifications :**

1. **ID correct dans le code**
```html
gtag('config', 'G-FL1S0MJWB1');  ← Vérifier ID
```

2. **CSP autorise GA4**
```toml
script-src 'self' 'unsafe-inline' https://www.googletagmanager.com;
connect-src 'self' https://www.google-analytics.com;
```

3. **Cookie banner fonctionnel**

Vérifier que le JS gère le consentement :
```javascript
// Dans assets/js/main.js
if (cookieConsent === 'accepted') {
  gtag('consent', 'update', {
    analytics_storage: 'granted'
  });
}
```

4. **Tester en Real-Time**

GA4 → Reports → Realtime → Voir si votre visite apparaît

### Problème : Menu mobile ne s'ouvre pas

**Cause :** JavaScript `main.js` non chargé ou erreur

**Vérifications :**

1. **Console navigateur** (F12)
```
Erreur : Cannot read property 'addEventListener' of null
```
→ Sélecteur DOM incorrect

2. **Vérifier ID/classes**
```html
<button id="burger">...</button>  ← ID doit matcher JS
<div id="menu-mobile">...</div>   ← ID doit matcher JS
```

3. **Vérifier script chargé**
```html
<script src="/assets/js/main.js"></script>  ← En fin de <body>
```

### Problème : Site inaccessible sur mobile

**Cause :** Meta viewport manquant ou incorrect

**Solution :**
```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

**Tester responsive :**
1. DevTools (F12) → Toggle device toolbar
2. Tester iPhone SE, iPad, Desktop
3. Vérifier menu burger visible < 768px

### Problème : Photos d'équipe ne s'affichent pas

**Symptôme :** Images cassées sur `/fr/team.html` ou `/de/team.html`

**Causes possibles :**

1. **Chemin relatif au lieu d'absolu**
```html
<!-- ❌ MAUVAIS (ne marche pas depuis /fr/team.html) -->
<img src="photoCV.png" />

<!-- ✅ BON (chemin absolu fonctionne partout) -->
<img src="/photoCV.png" />
```

2. **Fichier photo manquant**

Vérifier présence à la racine :
```bash
ls -la | grep photo
# Doit montrer : photoCV.png, photoURS.png, photo-bao.webp
```

**Solution :**
- Chemins doivent **toujours commencer par `/`** (absolu)
- Photos **à la racine** du repo (pas dans `/assets/images/`)
- Ou mieux : déplacer vers `/assets/images/team/` et mettre à jour HTML

**Structure recommandée :**
```
assets/images/
└── team/
    ├── arijanit.webp
    ├── bao.webp
    └── urs.webp
```

Puis dans HTML :
```html
<img src="/assets/images/team/arijanit.webp" alt="..." />
```

---

## 🔧 MAINTENANCE

### Modifier le CSS

**Fichier :** `/assets/css/main.css`

```bash
# 1. Éditer le fichier
nano assets/css/main.css

# 2. Tester localement (optionnel)
python3 -m http.server 8000
# Ouvrir http://localhost:8000/fr/

# 3. Push vers GitHub
git add assets/css/main.css
git commit -m "Update: CSS corrections"
git push origin main

# 4. Netlify déploie automatiquement (~1 min)
```

**Variables CSS importantes :**
```css
:root {
  --primary: #1a73e8;        /* Couleur principale (bleu) */
  --secondary: #f97316;      /* Couleur secondaire (orange) */
  --text: #1f2937;           /* Texte principal */
  --bg: #ffffff;             /* Fond */
}
```

### Modifier le JavaScript

**Fichier :** `/assets/js/main.js`

**Modules principaux :**
```javascript
// Menu burger mobile
const burger = document.getElementById('burger');
const menuMobile = document.getElementById('menu-mobile');

// Sélecteur langue
const langBtn = document.getElementById('lang-btn');
const langMenu = document.getElementById('lang-menu');

// Cookie banner
const cookieBanner = document.getElementById('cookie-banner');
const acceptBtn = document.getElementById('cookie-accept');
const refuseBtn = document.getElementById('cookie-refuse');
```

### Ajouter une page

#### 1. Créer le fichier HTML

```bash
# Copier une page existante comme template
cp fr/index.html fr/nouvelle-page.html
```

#### 2. Modifier le contenu

```html
<!-- Mettre à jour : -->
<title>Nouvelle page – Sophira</title>
<meta name="description" content="Description de la nouvelle page" />
<link rel="canonical" href="https://sophira.ch/fr/nouvelle-page.html" />

<!-- Mettre à jour hreflang -->
<link rel="alternate" hreflang="fr" href="https://sophira.ch/fr/nouvelle-page.html" />
<link rel="alternate" hreflang="de" href="https://sophira.ch/de/nouvelle-page.html" />
```

#### 3. Ajouter au menu

**Dans `/fr/index.html` et toutes les pages FR :**
```html
<nav class="primary">
  <a href="/fr/">Accueil</a>
  <a href="/fr/nouvelle-page.html">Nouvelle page</a>  ← AJOUTER
  <a href="/fr/team.html">Équipe</a>
  <!-- ... -->
</nav>
```

**Également dans le menu mobile :**
```html
<div id="menu-mobile" class="mobile-panel">
  <div class="mobile-links">
    <a href="/fr/">Accueil</a>
    <a href="/fr/nouvelle-page.html">Nouvelle page</a>  ← AJOUTER
    <!-- ... -->
  </div>
</div>
```

#### 4. Créer la version DE

```bash
cp de/index.html de/neue-seite.html
# Traduire le contenu en allemand
```

#### 5. Ajouter au sitemap

**Dans `sitemap.xml` :**
```xml
<url>
  <loc>https://sophira.ch/fr/nouvelle-page.html</loc>
  <lastmod>2026-03-08</lastmod>
  <xhtml:link rel="alternate" hreflang="fr" href="https://sophira.ch/fr/nouvelle-page.html" />
  <xhtml:link rel="alternate" hreflang="de" href="https://sophira.ch/de/neue-seite.html" />
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>

<url>
  <loc>https://sophira.ch/de/neue-seite.html</loc>
  <lastmod>2026-03-08</lastmod>
  <xhtml:link rel="alternate" hreflang="fr" href="https://sophira.ch/fr/nouvelle-page.html" />
  <xhtml:link rel="alternate" hreflang="de" href="https://sophira.ch/de/neue-seite.html" />
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

#### 6. Déployer

```bash
git add fr/nouvelle-page.html de/neue-seite.html sitemap.xml
git commit -m "Add: Nouvelle page FR/DE"
git push origin main
```

### Mettre à jour les images

#### 1. Optimiser l'image en WebP

```bash
# Outil recommandé : Squoosh.app ou cwebp

# Exemple avec cwebp (CLI)
cwebp -q 85 nouvelle-image.png -o assets/images/optimized/nouvelle-image.webp
```

#### 2. Garder l'original en fallback

```bash
cp nouvelle-image.png assets/images/fallback/
```

#### 3. Utiliser dans le HTML

```html
<picture>
  <source srcset="/assets/images/optimized/nouvelle-image.webp" type="image/webp">
  <img 
    src="/assets/images/fallback/nouvelle-image.png" 
    alt="Description" 
    width="800" 
    height="600"
    loading="lazy"
  >
</picture>
```

### Changer l'email de contact

**Fichiers à modifier :**

1. **Page privacy.html (FR et DE)**
```html
<p>Pour toute question : <a href="mailto:NOUVEAU_EMAIL">NOUVEAU_EMAIL</a></p>
```

2. **Page legal.html (FR et DE)**
```html
<p>Contact : <a href="mailto:NOUVEAU_EMAIL">NOUVEAU_EMAIL</a></p>
```

3. **Formulaire contact.html**
```html
<form action="https://formspree.io/f/NOUVEAU_ID" method="POST">
```

**Note :** Si vous utilisez Netlify Forms au lieu de Formspree :
```html
<form name="contact" netlify netlify-honeypot="bot-field">
```

### Mettre à jour Google Analytics

**Pour changer l'ID GA4 :**

1. **Chercher/remplacer dans toutes les pages**
```bash
grep -r "G-FL1S0MJWB1" .
# Remplacer par le nouvel ID
```

2. **Ou utiliser un script de config centralisé**

Créer `/assets/js/analytics.js` :
```javascript
const GA_ID = 'G-VOTRE-NOUVEL-ID';

gtag('js', new Date());
gtag('config', GA_ID);
```

Inclure dans toutes les pages :
```html
<script src="/assets/js/analytics.js"></script>
```

---

## 📚 HISTORIQUE DES PROBLÈMES RÉSOLUS

### Mars 2026 - Problèmes d'indexation Google

**Problème 1 : "Redirect error"**

**Symptôme :**
```
Page is not indexed: Redirect error
```

**Cause :**
1. Triple redirection dans `netlify.toml` (2 conditionnelles + 1 fallback)
2. Fichier `/index.html` à la racine avec meta refresh + JS redirect

**Solution :**
1. ✅ Remplacé les 3 redirections par 1 seule simple 301
2. ✅ Supprimé `/index.html` à la racine

**Commit :** `Fix: Suppression redirections conditionnelles pour Google`

**Fichiers modifiés :**
- `netlify.toml` (lignes 14-18 uniquement)
- **`/index.html` SUPPRIMÉ** (était à la racine, causait conflit)

---

**Problème 2 : "Googlebot blocked by robots.txt"**

**Symptôme :**
```
Page resources: 7/8 loaded
Script blocked: https://sophira.ch/assets/js/main.js
```

**Cause :** `robots.txt` contenait `Disallow: /assets/js/`

**Solution :**
```txt
# ✅ Remplacé par
Allow: /assets/
```

**Commit :** `Fix: robots.txt autorise assets JS/CSS pour Google`

---

**Problème 3 : Dashboards Tableau Public non visibles**

**Symptôme :** Iframes vides, erreur console CSP

**Cause :**
1. CSP bloquait `https://public.tableau.com`
2. Mauvais paramètres URL (`?:embed=yes` au lieu de `?embed=true`)

**Solution :**
1. ✅ Ajouté `frame-src https://public.tableau.com` dans CSP
2. ✅ Modifié format URL : `?:showVizHome=no&embed=true`

**Commit :** `Fix: CSP Tableau + format URL iframe correct`

---

**Problème 4 : Photos d'équipe cassées**

**Symptôme :** Photo Arijanit (`photoCV.png`) ne s'affiche pas sur page équipe

**Cause :** Chemin relatif incorrect dans HTML

```html
<!-- ❌ MAUVAIS (ne fonctionne pas) -->
<img src="photoCV.png" alt="..." />

<!-- ✅ BON (chemin absolu) -->
<img src="/photoCV.png" alt="..." />
```

**Solution :**
1. ✅ Corriger `/fr/team.html` : `src="/photoCV.png"`
2. ✅ Corriger `/de/team.html` : `src="/photoCV.png"`
3. ⏳ Uploader `photoURS.png` pour le trésorier

**Fichiers concernés :**
- `/fr/team.html` (ligne avec `photoCV.png`)
- `/de/team.html` (carte Urs à ajouter)

**Commit attendu :** `Fix: Chemins absolus photos équipe + ajout Urs`

---

### Améliorations de performance (Mars 2026)

**Optimisation 1 : Conversion images WebP**

**Avant :**
- `background.jpg` : 2.6 MB
- `Logo_sophira.png` : 450 KB
- `PHOTO-BAO.jpg` : 1.2 MB

**Après :**
- `background.webp` : 980 KB (-62%)
- `logo.webp` : 85 KB (-81%)
- `photo-bao.webp` : 320 KB (-73%)

**Commit :** `Perf: Images converties en WebP (-70% poids moyen)`

---

**Optimisation 2 : Consolidation CSS**

**Avant :** 24 blocs `<style>` inline dupliqués

**Après :** 1 fichier externe `/assets/css/main.css`

**Commit :** `Refactor: CSS consolidé en fichier unique`

---

**Optimisation 3 : Fonts self-hosted**

**Avant :** Google Fonts CDN (requête externe)

**Après :** Fonts locales WOFF2 (aucune requête externe)

**Commit :** `Perf: Fonts Inter self-hosted (RGPD + vitesse)`

---

### Sécurité (Mars 2026)

**Amélioration : Headers de sécurité complets**

**Ajouté dans `netlify.toml` :**
- Content Security Policy (CSP)
- HTTP Strict Transport Security (HSTS)
- X-Frame-Options, X-Content-Type-Options
- Permissions-Policy

**Commit :** `Security: Headers CSP + HSTS + Permissions-Policy`

---

## 📞 CONTACT ET SUPPORT

### Contacts projet

- **Email association :** association_sophira@protonmail.com
- **Site web :** https://sophira.ch
- **Repository GitHub :** https://github.com/medykrena/Sophira-website_v2

### Support technique

**Netlify :**
- Documentation : https://docs.netlify.com
- Support : https://answers.netlify.com

**Google Search Console :**
- Documentation : https://developers.google.com/search/docs
- Aide : https://support.google.com/webmasters

**Tableau Public :**
- Documentation : https://help.tableau.com/current/pro/desktop/en-us/embed.htm

---

## 📄 LICENCE

**Site web Sophira** - © 2026 Sophira Association  
**Code :** Propriétaire (usage interne uniquement)  
**Contenu :** Tous droits réservés

---

## 🔄 CHANGELOG

### Version 2.0 (Mars 2026)

**Nouveautés :**
- ✅ Refonte complète du site
- ✅ Structure bilingue FR/DE propre
- ✅ Optimisation performance (-85% poids page)
- ✅ SEO optimisé (hreflang, sitemap, redirections 301)
- ✅ Sécurité renforcée (CSP, HSTS)
- ✅ Dashboards Tableau Public intégrés
- ✅ Assistant ChatGPT GPT intégré
- ✅ Conformité LPD/RGPD (page privacy, cookie banner)

**Corrections :**
- ✅ Fix indexation Google (redirect error)
- ✅ Fix robots.txt (blocage JS/CSS)
- ✅ Fix CSP Tableau Public
- ✅ Fix format URL iframes Tableau

**Performance :**
- ✅ Images WebP optimisées (-62% poids moyen)
- ✅ CSS consolidé (1 fichier au lieu de 24)
- ✅ Fonts self-hosted (pas de CDN externe)
- ✅ Cache agressif assets (1 an)

---

## ✅ TODO LIST

### Priorité haute

- [ ] **Uploader `photoURS.png`** à la racine (photo trésorier)
- [ ] **Corriger `/fr/team.html`** : `src="photoCV.png"` → `src="/photoCV.png"` 
- [ ] **Corriger `/de/team.html`** : Ajouter carte Urs + corriger chemin photo
- [ ] Créer toutes les pages manquantes FR/DE
- [ ] Traduire articles blog en allemand
- [ ] Tester formulaires contact/newsletter
- [ ] Configurer Netlify Forms ou Formspree
- [ ] Vérifier indexation Google (toutes pages)
- [ ] Tester responsive sur vrais devices (iOS, Android)

🎯 AMÉLIORATIONS SEO
- [ ] Schema.org complet : Google comprend mieux la structure
- [ ] Alt text descriptif : Meilleure accessibilité
- [ ] Nom propre dans h3 : Structure sémantique correcte
- [ ] Extension .png : Image sera chargée correctement

### Priorité moyenne

- [ ] Ajouter Schema.org structured data (LocalBusiness, FAQPage)
- [ ] Optimiser images supplémentaires (article blog, équipe)
- [ ] Ajouter tests automatisés (Lighthouse CI)
- [ ] Configurer monitoring uptime (UptimeRobot)
- [ ] Créer page `/jobs/` fonctionnelle

### Priorité basse

- [ ] Ajouter dark mode
- [ ] Internationalisation i18n (EN)
- [ ] Progressive Web App (PWA)
- [ ] Animations CSS avancées
- [ ] Service Worker (cache offline)

---

**Dernière mise à jour :** 8 mars 2026  
**Version README :** 2.0  
**Maintenu par :** Équipe Sophira
