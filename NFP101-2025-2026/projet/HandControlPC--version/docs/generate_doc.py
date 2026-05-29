"""
Génère la documentation PDF du projet HandControlPC.
Lancer : python docs/generate_doc.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)

OUTPUT = "docs/HandControlPC_Documentation.pdf"

def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=2.5*cm, rightMargin=2.5*cm,
        topMargin=2.5*cm, bottomMargin=2.5*cm
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle("Title2", parent=styles["Title"],
                                  fontSize=22, spaceAfter=6, textColor=colors.HexColor("#1a237e"))
    h1_style = ParagraphStyle("H1", parent=styles["Heading1"],
                               fontSize=14, spaceAfter=4, textColor=colors.HexColor("#283593"))
    h2_style = ParagraphStyle("H2", parent=styles["Heading2"],
                               fontSize=12, spaceAfter=3, textColor=colors.HexColor("#3949ab"))
    body = styles["Normal"]
    code_style = ParagraphStyle("Code", parent=styles["Code"],
                                 fontSize=9, fontName="Courier",
                                 backColor=colors.HexColor("#f5f5f5"),
                                 leftIndent=12, rightIndent=12,
                                 spaceAfter=6)
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=20, spaceAfter=2)

    story = []

    # ------------------------------------------------------------------
    # Page de titre
    # ------------------------------------------------------------------
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("HandControlPC", title_style))
    story.append(Paragraph("Contrôle gestuel du PC par webcam", styles["Heading2"]))
    story.append(Spacer(1, 0.4*cm))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1a237e")))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("Documentation technique — Projet POO NFP101", body))
    story.append(Paragraph("Auteur : Mohamed Amine Sobhi", body))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "IA utilisée : Claude Code (Anthropic) — voir section 5 pour les détails.", body))
    story.append(PageBreak())

    # ------------------------------------------------------------------
    # 1. Contexte et besoin
    # ------------------------------------------------------------------
    story.append(Paragraph("1. Contexte et besoin", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#3949ab")))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "Les interfaces homme-machine traditionnelles reposent sur le clavier et la souris. "
        "HandControlPC propose une alternative : contrôler son PC via des gestes de la main "
        "captés par la webcam, sans matériel supplémentaire.", body))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Cas d'usage :", body))
    for item in [
        "Contrôle du volume audio sans toucher le clavier",
        "Prise de capture d'écran sans raccourci clavier",
        "Zoom sur le flux vidéo via geste bimanuel",
        "Reconnaissance de signes (A, B, L) pour accessibilité",
    ]:
        story.append(Paragraph(f"• {item}", bullet))
    story.append(Spacer(1, 0.3*cm))

    # ------------------------------------------------------------------
    # 2. Fonctionnalités
    # ------------------------------------------------------------------
    story.append(Paragraph("2. Fonctionnalités", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#3949ab")))
    story.append(Spacer(1, 0.2*cm))

    data = [
        ["Geste", "Action", "Retour au menu"],
        ["Index seul levé", "Mode Volume : pincement pouce-index", "Main ouverte (5 doigts)"],
        ["3 doigts levés", "Mode Screenshot : maintenir ~0.7s", "Automatique après capture"],
        ["2 mains visibles", "Mode Zoom : écarter/rapprocher les index", "Une seule main restante"],
    ]
    t = Table(data, colWidths=[4.5*cm, 7*cm, 4.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#283593")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#e8eaf6")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("2.1 Reconnaissance de signes", h2_style))
    story.append(Paragraph(
        "Le module test_sign_recognition.py implémente la reconnaissance statique "
        "de 3 signes de la main (A, B, L) avec stabilisation temporelle "
        "(HOLD_FRAMES = 20 frames) et retour vocal (commande say de macOS).", body))
    story.append(Spacer(1, 0.3*cm))

    # ------------------------------------------------------------------
    # 3. Architecture et choix techniques
    # ------------------------------------------------------------------
    story.append(Paragraph("3. Architecture et choix techniques", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#3949ab")))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("3.1 Structure des modules", h2_style))
    story.append(Paragraph(
        "Le projet est organisé en modules indépendants :", body))
    modules = [
        ("main.py", "Point d'entrée — boucle principale, gestion des modes"),
        ("utils/gesture_action.py", "Classe abstraite GestureAction (ABC) — interface commune"),
        ("utils/hand_tracking.py", "HandDetector — détection MediaPipe et calcul fingers_up"),
        ("utils/volume_control.py", "VolumeController — hérite de GestureAction"),
        ("utils/screenshot.py", "ScreenshotTaker — hérite de GestureAction"),
        ("utils/zoom_control.py", "ZoomManager — hérite de GestureAction"),
        ("utils/config_loader.py", "Chargement JSON avec deepcopy et fallback"),
        ("config.json", "Configuration externe modifiable sans toucher au code"),
        ("tests/", "22 tests unitaires automatisés avec pytest"),
    ]
    mod_data = [["Fichier", "Rôle"]] + [[m, r] for m, r in modules]
    mt = Table(mod_data, colWidths=[7*cm, 9*cm])
    mt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#283593")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Courier"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#e8eaf6")]),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(mt)
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("3.2 Héritage et polymorphisme", h2_style))
    story.append(Paragraph(
        "La classe abstraite GestureAction définit le contrat commun à toutes les actions :", body))
    story.append(Paragraph(
        "• Méthode abstraite process(img, hands_data) → implémentée par chaque sous-classe", bullet))
    story.append(Paragraph(
        "• Méthodes concrètes activate(), deactivate(), render_hud() — partagées par héritage", bullet))
    story.append(Paragraph(
        "• Polymorphisme : main.py appelle process() sans connaître le type exact de l'action", bullet))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Hiérarchie :", body))
    story.append(Paragraph(
        "GestureAction (ABC)\n"
        "├── VolumeController\n"
        "├── ScreenshotTaker\n"
        "└── ZoomManager", code_style))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("3.3 Bibliothèques choisies", h2_style))
    libs = [
        ("OpenCV", "Capture webcam, traitement d'image, affichage HUD"),
        ("MediaPipe", "Détection 21 landmarks de la main en temps réel"),
        ("NumPy", "Interpolation linéaire (volume), clipping (zoom)"),
        ("MSS", "Capture d'écran multi-plateforme"),
        ("osascript", "Contrôle volume et son macOS natif"),
        ("pytest", "Framework de tests unitaires"),
        ("reportlab", "Génération de la documentation PDF"),
    ]
    lib_data = [["Bibliothèque", "Justification"]] + libs
    lt = Table(lib_data, colWidths=[4*cm, 12*cm])
    lt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#283593")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#e8eaf6")]),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(lt)
    story.append(Spacer(1, 0.3*cm))

    # ------------------------------------------------------------------
    # 4. Tests
    # ------------------------------------------------------------------
    story.append(Paragraph("4. Tests unitaires", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#3949ab")))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "22 tests automatisés dans tests/ — tous exécutables sans webcam ni matériel :", body))
    test_items = [
        "Reconnaissance de signes (A, B, L, inconnus)",
        "Interpolation volume (distance → pourcentage)",
        "Calcul de distance euclidienne",
        "Reset et clipping du ZoomManager",
        "Vérification de l'héritage (isinstance GestureAction)",
        "Chargement config JSON, fallback sur valeurs par défaut, JSON invalide",
        "Création du dossier screenshots",
        "Comportement de fingers_up avec données vides",
    ]
    for item in test_items:
        story.append(Paragraph(f"• {item}", bullet))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Commande d'exécution :", body))
    story.append(Paragraph("python -m pytest tests/ -v", code_style))
    story.append(Spacer(1, 0.3*cm))

    # ------------------------------------------------------------------
    # 5. Utilisation de l'IA
    # ------------------------------------------------------------------
    story.append(Paragraph("5. Utilisation de l'IA", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#3949ab")))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        "L'IA utilisée est Claude Code (Anthropic — claude-sonnet-4-6). "
        "Tout le code généré est encadré dans le source avec les marqueurs requis :", body))
    story.append(Paragraph(
        "# ############### CODE IA (Claude) ################", code_style))
    story.append(Spacer(1, 0.2*cm))

    ai_data = [
        ["Ce qui a été généré/aidé par IA", "Prompt / Description", "Ce que j'ai modifié/validé"],
        [
            "Classe abstraite GestureAction",
            "\"Crée une classe de base ABC en Python pour des actions gestuelles avec process() abstraite et render_hud() commune\"",
            "Adapté les signatures, vérifié la compatibilité avec les sous-classes existantes"
        ],
        [
            "Refactorisation VolumeController, ScreenshotTaker, ZoomManager",
            "\"Fais hériter ces classes de GestureAction en implémentant process()\"",
            "Validé que la logique métier (calcul distance, capture) reste inchangée"
        ],
        [
            "Module config_loader.py",
            "\"Crée un loader JSON avec deepcopy et fallback sur valeurs par défaut\"",
            "Identifié et corrigé le bug de shallow copy (merged[section].update modifiait _DEFAULT_CONFIG)"
        ],
        [
            "Suite de tests pytest (22 tests)",
            "\"Génère des tests unitaires sans webcam pour fingers_up, recognize_sign, ZoomManager, config\"",
            "Ajouté les cas de test sur l'héritage, supprimé les tests nécessitant du matériel"
        ],
        [
            "Documentation PDF (ce fichier)",
            "\"Génère un script reportlab pour la documentation technique du projet\"",
            "Rédigé le contenu (contexte, fonctionnalités, limites)"
        ],
    ]
    at = Table(ai_data, colWidths=[4.5*cm, 6*cm, 5.5*cm])
    at.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#283593")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#e8eaf6")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("WORDWRAP", (0, 0), (-1, -1), True),
    ]))
    story.append(at)
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "Taux estimé d'utilisation IA : ~35% (architecture et tests). "
        "La logique de détection gestuelle, la boucle principale, et l'intégration "
        "MediaPipe/OpenCV ont été écrits et maîtrisés par l'auteur.", body))
    story.append(Spacer(1, 0.3*cm))

    # ------------------------------------------------------------------
    # 6. Limites et pistes d'amélioration
    # ------------------------------------------------------------------
    story.append(Paragraph("6. Limites et pistes d'amélioration", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#3949ab")))
    story.append(Spacer(1, 0.2*cm))
    limits = [
        "Limité à macOS (osascript, afplay) — portage Windows/Linux nécessite des alternatives",
        "Sensible à la luminosité et aux arrière-plans complexes",
        "Reconnaissance de signes limitée à 3 lettres (A, B, L)",
        "Pas de contrôle de la souris ou des fenêtres (prévu comme amélioration)",
    ]
    improvements = [
        "Ajout du déplacement de souris par geste (index pointant)",
        "Support Windows/Linux via des APIs cross-platform",
        "Ajout d'un mode apprentissage pour enregistrer de nouveaux gestes",
        "Interface de configuration graphique (tkinter ou web)",
        "Système de logs persistants dans un fichier",
    ]
    story.append(Paragraph("Limites actuelles :", body))
    for item in limits:
        story.append(Paragraph(f"• {item}", bullet))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph("Pistes d'amélioration :", body))
    for item in improvements:
        story.append(Paragraph(f"• {item}", bullet))

    doc.build(story)
    print(f"Documentation générée : {OUTPUT}")


if __name__ == "__main__":
    build()
