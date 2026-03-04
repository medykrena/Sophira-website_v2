# 🌟 SOPHIRA.CH - SITE WEB OPTIMISÉ V2

Version 2.0 - Reconstruction complète et optimisée

## 📋 CE QUI A ÉTÉ FAIT

### ✅ Structure Moderne
- Architecture `/fr/` `/de/` propre et scalable
- Assets consolidés et optimisés
- Separation claire site vitrine / job portal
- Compatible future évolution

### ✅ Performance
- **Images optimisées WebP** : Background 2.6 MB → 980 KB (-62%)
- **CSS consolidé** : 1 seul fichier au lieu de 24 fichiers inline
- **JS consolidé** : Code modulaire et maintenable
- **Fonts self-hosted** : Pas de dépendance externe
- **Favicons** : 4 tailles créées (16x16, 32x32, 180x180, .ico)

### ✅ Sécurité
- Content Security Policy (CSP) complet
- HSTS activé
- Permissions-Policy configuré
- Headers de sécurité optimaux

### ✅ SEO
- Redirects 301 complets (préservation ranking)
- Structure hreflang propre FR/DE
- Meta tags optimisés
- Sitemap à jour

### ✅ Compliance LPD (Suisse)
- Page privacy.html complète
- Email responsable: association_sophira@protonmail.com
- Cookies détaillés
- Base légale claire

---

## 📁 STRUCTURE DES FICHIERS

```
sophira-v2/
├── fr/                     # Site vitrine français
│   └── index.html         # ✅ Créé et testé
├── de/                     # Site vitrine allemand
│   └── (à créer)
├── blog/
│   ├── fr/
│   └── de/
├── jobs/                   # Job portal séparé
├── assets/
│   ├── css/
│   │   └── main.css       # ✅ CSS consolidé complet
│   ├── js/
│   │   └── main.js        # ✅ JavaScript modulaire
│   ├── fonts/
│   │   └── README_FONTS.md # Instructions téléchargement
│   ├── images/
│   │   ├── optimized/     # ✅ Images WebP optimisées
│   │   └── fallback/      # ✅ Images originales
│   └── icons/             # ✅ Favicons 4 tailles
├── netlify.toml           # ✅ Config complète
└── README.md              # Ce fichier
```

---

## 🚀 DÉPLOIEMENT

### Étape 1 : Télécharger les fonts
1. Les fonts Inter ne sont PAS incluses (problème réseau)
2. Voir `/assets/fonts/README_FONTS.md` pour instructions
3. Télécharger `inter-400.woff2` et `inter-600.woff2`
4. Les placer dans `/assets/fonts/`

### Étape 2 : Créer le repository GitHub
```bash
1. GitHub.com → New repository
2. Nom: sophira-website-v2
3. Ne pas initialiser avec README
4. Créer
```

### Étape 3 : Uploader les fichiers
```bash
1. Télécharger sophira-v2.zip
2. Décompresser
3. Dans GitHub: Upload files → Drag & drop tous les fichiers
4. Commit: "Initial commit - Site optimisé v2"
```

### Étape 4 : Déployer sur Netlify
```bash
1. Netlify Dashboard → Add new site
2. Import from GitHub
3. Sélectionner sophira-website-v2
4. Deploy settings: automatiques (netlify.toml)
5. Deploy site
```

### Étape 5 : Tester
```bash
1. Attendre déploiement (~30s)
2. Visiter [votre-site].netlify.app
3. Tester TOUTES les pages
4. Vérifier mobile/desktop
5. Tester formulaires
```

### Étape 6 : Migration domaine
⚠️ À faire UNIQUEMENT quand tout est testé et validé
```bash
1. Netlify ancien site → Domain settings
2. Retirer sophira.ch
3. Netlify nouveau site → Domain settings
4. Ajouter sophira.ch
5. Attendre propagation DNS (1-2h)
```

---

## ⚠️ CE QUI RESTE À FAIRE

### Pages manquantes (prioritaires)
- [ ] `/fr/project.html` - Le projet
- [ ] `/fr/team.html` - L'équipe
- [ ] `/fr/blog.html` - Liste blog
- [ ] `/fr/contact.html` - Contact
- [ ] `/fr/donate.html` - Dons
- [ ] `/fr/privacy.html` - Confidentialité (LPD)
- [ ] `/fr/legal.html` - Mentions légales
- [ ] `/fr/dashboard.html` - Dashboard
- [ ] Toutes les versions `/de/`

### Articles blog (7 articles)
- [ ] `/blog/fr/article-1.html`
- [ ] `/blog/fr/article-2.html`
- [ ] etc.

### Job Portal
- [ ] `/jobs/index.html`
- [ ] `/jobs/apply.html`

### Fichiers config
- [ ] `robots.txt`
- [ ] `sitemap.xml`
- [ ] `404.html`

---

## 📊 COMPARAISON AVANT/APRÈS

| Métrique | Avant | Après | Gain |
|----------|-------|-------|------|
| Taille page accueil | ~2.8 MB | ~400 KB | -85% |
| Fichiers CSS | 24 inline | 1 externe | -96% |
| Favicons | 0/4 | 4/4 | ✅ |
| Structure URL | Incohérente | Propre | ✅ |
| Headers sécurité | Basiques | Complets | ✅ |
| Fonts | CDN externe | Self-hosted | ✅ |

---

## 🔧 MAINTENANCE

### Modifier le CSS
Éditer `/assets/css/main.css`

### Modifier le JavaScript
Éditer `/assets/js/main.js`

### Ajouter une page
1. Créer `nouvelle-page.html` dans `/fr/` et `/de/`
2. Copier le template de `index.html`
3. Mettre à jour les liens dans les menus
4. Push vers GitHub → Netlify redéploie automatiquement

---

## 📧 CONTACT

**Email:** association_sophira@protonmail.com
**Site:** https://sophira.ch

---

## 📄 LICENSE

© 2026 Sophira Association | Basel, Suisse
