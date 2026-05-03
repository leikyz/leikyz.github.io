#!/usr/bin/env python3
"""
Generates one HTML file per project in /home/claude/output/leikyz.github.io/projects/
using a shared structure. Each project page includes:
 - Header (copied style from index, relative links adjusted with ../)
 - Breadcrumb
 - Hero with title, subtitle, badges, tags
 - Media (video or image)
 - Content (FR + EN variants with data-lang-* attrs)
 - Sidebar: info card + stack + chain (for bundle projects)
 - Nav footer (prev/next)
 - Language switcher JS (same as index)
"""

import os
import json

OUTPUT_DIR = "/home/claude/output/leikyz.github.io/projects"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- Project data ----------
# Each project has:
#   slug, title_fr, title_en, subtitle_fr, subtitle_en,
#   year, status (wip/done/duration),
#   people_fr, people_en,
#   tags (list), stack (list for sidebar),
#   media: {type: 'video'|'image'|'placeholder', src: '...' or icon}
#   body_fr, body_en (HTML allowed)
#   bundle: None or dict { name_fr, name_en, steps: [(slug, title, step_label)], current_index: N }
#   prev, next: None or (slug, title) tuples for nav footer

PROJECTS = [
    # ---------- BUNDLE 01: Multiplayer Ecosystem ----------
    {
        "slug": "lkz-network",
        "title_fr": "LKZ Network",
        "title_en": "LKZ Network",
        "subtitle_fr": "Moteur réseau léger, efficace et haute performance pour le multijoueur en temps réel sur Windows et Linux.",
        "subtitle_en": "Efficient lightweight, high-performance networking engine for real-time multiplayer on Windows and Linux.",
        "year": "2025",
        "status_badge": "WIP",
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Développeur solo",
        "role_en": "Solo developer",
        "tags": ["C++", "Multithread", "Serialization", "ECS", "IOCP", "UDP", "Matchmaking", "Lobby"],
        "stack": ["C++", "IOCP", "UDP", "Multithread", "ECS"],
        "step_label": "step_01 // engine",
        "bundle_id": "multiplayer-ecosystem",
        "media": {"type": "video", "src": "../assets/videos/lkznetwork.mp4", "poster": "../assets/images/projects/lkznetwork.png"},
        "body_fr": """<p>J'ai commencé à apprendre la programmation réseau en octobre 2024, en débutant avec un moteur réseau C# basé sur TCP. Cette première version m'a permis de synchroniser deux joueurs dans Unity, ce qui m'a aidé à comprendre les fondamentaux de la communication client-serveur, de la latence et du flux de paquets.</p>
<p>Après avoir expérimenté avec TCP, j'ai adapté le moteur pour utiliser UDP, afin de mieux comprendre les défis de la fiabilité, de la perte de paquets et de la synchronisation en temps réel — une étape cruciale vers la construction de systèmes multijoueurs performants.</p>
<p>En février 2025, j'ai décidé de me spécialiser dans le développement réseau et de tout reconstruire à partir de zéro en C++, en me concentrant sur l'optimisation bas niveau, la scalabilité et une architecture multijoueur de qualité professionnelle.</p>
<h4>Fonctionnalités Actuelles</h4>
<ul>
  <li>Système de Sérialisation / Désérialisation pour un échange de données rapide</li>
  <li>Optimisation des paquets pour réduire la charge réseau et améliorer l'efficacité de la bande passante</li>
  <li>Architecture légère, conçue pour les jeux en réseau temps réel</li>
  <li>Multithreading avec un contrôle de concurrence fin</li>
  <li>Protocole IOCP (Windows) pour des E/S asynchrones et scalables</li>
  <li>Couche de communication UDP pour une transmission de données à faible latence</li>
  <li>Gestion réseau événementielle pour des opérations asynchrones propres</li>
  <li>Système de Matchmaking, Lobby, Client et gestion des entités</li>
  <li>Intégration ECS (Entity Component System) pour des mises à jour d'entités efficaces</li>
  <li>Autorité serveur complète pour garantir une simulation déterministe et sécurisée</li>
</ul>
<h4>Objectifs Futurs</h4>
<ul>
  <li>Paquets chiffrés pour une transmission de données sécurisée</li>
  <li>Fragmentation et réassemblage des paquets pour supporter de grandes charges de données</li>
  <li>Authentification cryptographiquement sécurisée via des jetons de connexion</li>
  <li>Support Linux via XDP pour un traitement de paquets à très faible latence</li>
  <li>Messagerie non fiable et non ordonnée pour les données sensibles au temps (ex: position, physique)</li>
</ul>""",
        "body_en": """<p>I began learning network programming in October 2024, starting with a C# TCP-based network engine. This early version allowed me to synchronize two players in Unity, which helped me understand the fundamentals of client-server communication, latency, and packet flow.</p>
<p>After experimenting with TCP, I adapted the engine to use UDP, to better understand the challenges of reliability, packet loss, and real-time synchronization — a crucial step toward building performant multiplayer systems.</p>
<p>By February 2025, I decided to specialize in network development and rebuild everything from scratch in C++, focusing on low-level optimization, scalability, and industry-grade multiplayer architecture.</p>
<h4>Current Features</h4>
<ul>
  <li>Serialization / Deserialization system for fast data exchange</li>
  <li>Packet Optimization to reduce network load and improve bandwidth efficiency</li>
  <li>Lightweight Architecture, built for real-time game networking</li>
  <li>Multithreading with fine-grained concurrency control</li>
  <li>IOCP Protocol (Windows) for scalable asynchronous I/O</li>
  <li>UDP Communication Layer for low-latency data transmission</li>
  <li>Event-driven Network Handling for clean async operations</li>
  <li>Matchmaking System, Lobby, Client, and Entity Management</li>
  <li>ECS (Entity Component System) for efficient entity updates</li>
  <li>Full Server Authority to ensure deterministic and secure simulation</li>
</ul>
<h4>Future Goals</h4>
<ul>
  <li>Encrypted Packets for secure data transmission</li>
  <li>Packet Fragmentation and Reassembly to support large data payloads</li>
  <li>Cryptographically Secure Authentication using connection tokens</li>
  <li>Linux Support via XDP for ultra-low latency packet processing</li>
  <li>Unreliable-Unordered Messaging for time-sensitive data (e.g., position and physics updates)</li>
</ul>""",
    },
    {
        "slug": "lkz-online-services",
        "title_fr": "LKZ Online Services",
        "title_en": "LKZ Online Services",
        "subtitle_fr": "Couche de services en ligne reliant Dead Protocol à LKZ Network — sessions, profils joueurs et état global.",
        "subtitle_en": "Online services layer bridging Dead Protocol with LKZ Network — sessions, player profiles, and global state.",
        "year": "2025",
        "status_badge": "WIP",
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Développeur solo",
        "role_en": "Solo developer",
        "tags": ["C#", "C++", "Online Services", "API"],
        "stack": ["C#", "C++", "REST API"],
        "step_label": "step_02 // services",
        "bundle_id": "multiplayer-ecosystem",
        "media": {"type": "placeholder", "src": "{ online_services }"},
        "body_fr": """<p>LKZ Online Services est la couche de services persistants qui connecte Dead Protocol à LKZ Network. Elle orchestre tout ce qui dépasse la simple connexion réseau : gestion des sessions de jeu, profils joueurs, et synchronisation de l'état global.</p>
<h4>Fonctionnalités</h4>
<ul>
  <li><strong>Gestion des Sessions :</strong> Orchestration des sessions de jeu entre les clients et le serveur LKZ Network.</li>
  <li><strong>Profils Joueurs :</strong> Stockage et récupération des données de progression.</li>
  <li><strong>État Global :</strong> Synchronisation de l'état global entre les composants du système.</li>
  <li><strong>API de Communication :</strong> Interface standardisée entre Dead Protocol (C#) et LKZ Network (C++).</li>
</ul>""",
        "body_en": """<p>LKZ Online Services is the persistent services layer connecting Dead Protocol to LKZ Network. It orchestrates everything beyond raw networking: game session management, player profiles, and global state synchronization.</p>
<h4>Features</h4>
<ul>
  <li><strong>Session Management:</strong> Orchestration of game sessions between clients and the LKZ Network server.</li>
  <li><strong>Player Profiles:</strong> Storage and retrieval of player progression data.</li>
  <li><strong>Global State:</strong> Synchronization of global state between system components.</li>
  <li><strong>Communication API:</strong> Standardized interface between Dead Protocol (C#) and LKZ Network (C++).</li>
</ul>""",
    },
    {
        "slug": "dead-protocol",
        "title_fr": "Dead Protocol",
        "title_en": "Dead Protocol",
        "subtitle_fr": "Jeu de tir à la troisième personne multijoueur utilisant LKZ Network.",
        "subtitle_en": "Multiplayer third-person shooter powered by LKZ Network.",
        "year": "2025",
        "status_badge": "WIP",
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Développeur solo",
        "role_en": "Solo developer",
        "tags": ["C#", "Unity", "Procedural Animation", "Multiplayer"],
        "stack": ["C#", "Unity", "Multiplayer"],
        "step_label": "step_03 // game",
        "bundle_id": "multiplayer-ecosystem",
        "media": {"type": "video", "src": "../assets/videos/deadprotocol.mp4", "poster": "../assets/images/projects/deadprotocol.png"},
        "body_fr": """<p>Dead Protocol est un jeu de tir à la troisième personne (TPS) multijoueur, conçu pour des équipes jusqu'à 4 joueurs. S'inspirant du style de jeu dynamique de Call of Duty Zombies, il plonge les joueurs dans une lutte intense pour la survie. Grâce à l'intégration de mon moteur réseau haute performance, LKZ Network, le jeu peut synchroniser des centaines d'entités simultanément, créant une immersion totale face à des hordes massives de zombies.</p>
<h4>Fonctionnalités Actuelles</h4>
<ul>
  <li><strong>IA en Réseau :</strong> Des zombies avec un comportement de poursuite entièrement synchronisé sur le réseau.</li>
  <li><strong>Synchronisation Avancée :</strong> Mouvements et animations des personnages répliqués avec précision pour tous les joueurs.</li>
  <li><strong>Animations Procédurales :</strong> Système d'animation procédurale pour une gestion réaliste et fluide de la visée et du maniement des armes.</li>
  <li><strong>Outil de Création d'Armes :</strong> Un outil de création d'armes poussé pour configurer et adapter facilement tout type d'arme à feu.</li>
  <li><strong>Architecture Client-Serveur :</strong> Un client C# (Unity) optimisé pour communiquer efficacement avec le serveur C++ (LKZ Network).</li>
  <li><strong>Optimisation Réseau :</strong> Envoi et réception de paquets optimisés pour garantir une faible latence et une expérience de jeu fluide.</li>
</ul>
<h4>Objectifs Futurs</h4>
<ul>
  <li><strong>Hordes Massives :</strong> Intégration de hordes dynamiques inspirées de Days Gone, gérant des milliers d'ennemis simultanément.</li>
  <li><strong>Progression et Atouts :</strong> Système de 'Power-ups' et d'atouts (perks) à la CoD Zombies pour améliorer les capacités des joueurs.</li>
  <li><strong>Objectifs Évolutifs :</strong> Missions dynamiques et secrets à découvrir sur la carte pour enrichir l'expérience.</li>
  <li><strong>Boss Uniques :</strong> Introduction de boss spéciaux avec des mécaniques de combat complexes.</li>
</ul>""",
        "body_en": """<p>Dead Protocol is a multiplayer third-person shooter (TPS) designed for teams of up to 4 players. Inspired by the dynamic gameplay of Call of Duty Zombies, it immerses players in an intense struggle for survival. By integrating my high-performance network engine, LKZ Network, the game can synchronize hundreds of entities simultaneously, creating total immersion against massive zombie hordes.</p>
<h4>Current Features</h4>
<ul>
  <li><strong>Networked AI:</strong> Zombies with fully synchronized chasing behavior over the network.</li>
  <li><strong>Advanced Synchronization:</strong> Character movements and animations are accurately replicated for all players.</li>
  <li><strong>Procedural Animations:</strong> A procedural animation system for realistic and fluid aiming and weapon handling.</li>
  <li><strong>Weapon Creation Tool:</strong> An advanced weapon creation tool to easily configure and adapt any type of firearm.</li>
  <li><strong>Client-Server Architecture:</strong> A C# client (Unity) optimized to communicate efficiently with the C++ server (LKZ Network).</li>
  <li><strong>Network Optimization:</strong> Optimized packet sending and receiving to ensure low latency and a smooth gaming experience.</li>
</ul>
<h4>Future Goals</h4>
<ul>
  <li><strong>Massive Hordes:</strong> Integration of dynamic hordes inspired by Days Gone, managing hundreds of enemies simultaneously.</li>
  <li><strong>Progression and Perks:</strong> A system of 'Power-ups' and perks like in CoD Zombies to enhance player abilities.</li>
  <li><strong>Evolving Objectives:</strong> Dynamic missions and secrets to discover on the map to enrich the experience.</li>
  <li><strong>Unique Bosses:</strong> Introduction of special bosses with complex combat mechanics.</li>
</ul>""",
    },
    # ---------- BUNDLE 02: Heist Day ----------
    {
        "slug": "heist-day-matchmaker",
        "title_fr": "heist-day-matchmaker",
        "title_en": "heist-day-matchmaker",
        "subtitle_fr": "Backend de matchmaking en Go pour Heist Day — gestion des lobbies, équilibrage des équipes et orchestration des sessions.",
        "subtitle_en": "Go matchmaking backend for Heist Day — lobby management, team balancing, and session orchestration.",
        "year": "2025",
        "status_badge": "WIP",
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Développeur backend",
        "role_en": "Backend developer",
        "tags": ["Go", "REST API", "Matchmaking", "Backend"],
        "stack": ["Go", "REST API", "EOS"],
        "step_label": "step_01 // backend",
        "bundle_id": "heist-day",
        "media": {"type": "placeholder", "src": "{ matchmaker.go }"},
        "body_fr": """<p>heist-day-matchmaker est le serveur backend en Go qui orchestre le matchmaking de Heist Day. Il s'interface avec Epic Online Services et gère la création des parties côté serveur.</p>
<h4>Fonctionnalités</h4>
<ul>
  <li><strong>Gestion des Lobbies :</strong> Création et gestion des salles d'attente avant les parties.</li>
  <li><strong>Équilibrage :</strong> Algorithme d'équilibrage basé sur le niveau des joueurs.</li>
  <li><strong>Orchestration des Sessions :</strong> Communication avec EOS pour la création et gestion des sessions.</li>
  <li><strong>API REST :</strong> Interface HTTP exposée au client UE5 pour le matchmaking.</li>
</ul>""",
        "body_en": """<p>heist-day-matchmaker is the Go backend server orchestrating matchmaking for Heist Day. It interfaces with Epic Online Services and handles game creation server-side.</p>
<h4>Features</h4>
<ul>
  <li><strong>Lobby Management:</strong> Creation and management of pre-match waiting rooms.</li>
  <li><strong>Team Balancing:</strong> Balancing algorithm based on player skill.</li>
  <li><strong>Session Orchestration:</strong> Communication with EOS for session creation and management.</li>
  <li><strong>REST API:</strong> HTTP interface exposed to the UE5 client for matchmaking.</li>
</ul>""",
    },
    {
        "slug": "heist-day",
        "title_fr": "Heist Day",
        "title_en": "Heist Day",
        "subtitle_fr": "Jeu d'action multijoueur en Unreal Engine 5 utilisant Epic Online Services pour la gestion des sessions et le matchmaking.",
        "subtitle_en": "Multiplayer action game built in Unreal Engine 5, using Epic Online Services for session management and matchmaking.",
        "year": "2025",
        "status_badge": "WIP",
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Développeur solo",
        "role_en": "Solo developer",
        "tags": ["C++", "UE5", "EOS", "Multiplayer", "Gameplay"],
        "stack": ["C++", "UE5", "Blueprint", "EOS"],
        "step_label": "step_02 // game",
        "bundle_id": "heist-day",
        "media": {"type": "placeholder", "src": "{ heist_day.exe }"},
        "body_fr": """<p>Heist Day est un jeu d'action multijoueur développé en Unreal Engine 5. Il utilise Epic Online Services (EOS) pour la gestion des sessions et s'appuie sur un backend Go dédié pour le matchmaking.</p>
<h4>Architecture</h4>
<ul>
  <li><strong>Client UE5 :</strong> Gameplay, rendu et interface développés en C++ et Blueprint.</li>
  <li><strong>Epic Online Services :</strong> Gestion des sessions, authentification et présence des joueurs via EOS.</li>
  <li><strong>Backend Matchmaking :</strong> Serveur Go (heist-day-matchmaker) pour l'équilibrage et l'orchestration des parties.</li>
</ul>""",
        "body_en": """<p>Heist Day is a multiplayer action game developed in Unreal Engine 5. It uses Epic Online Services (EOS) for session management and relies on a dedicated Go backend for matchmaking.</p>
<h4>Architecture</h4>
<ul>
  <li><strong>UE5 Client:</strong> Gameplay, rendering, and UI developed in C++ and Blueprint.</li>
  <li><strong>Epic Online Services:</strong> Session management, authentication, and player presence via EOS.</li>
  <li><strong>Matchmaking Backend:</strong> Go server (heist-day-matchmaker) for team balancing and game orchestration.</li>
</ul>""",
    },
    # ---------- OTHER PROJECTS ----------
    {
        "slug": "extraction-z",
        "title_fr": "Extraction Z",
        "title_en": "Extraction Z",
        "subtitle_fr": "FPS compétitif, mêlant jeu d'équipe et survie face aux zombies.",
        "subtitle_en": "Competitive FPS, blending team play and zombie survival.",
        "year": "2025",
        "status_badge_type": "duration",
        "status_badge_fr": "8 semaines",
        "status_badge_en": "8 weeks",
        "people_fr": "8 personnes",
        "people_en": "8 persons",
        "role_fr": "Gameplay / Réseau",
        "role_en": "Gameplay / Networking",
        "tags": ["C#", "Unity", "Multiplayer", "ECS", "Netcode for Entities", "Wwise"],
        "stack": ["C#", "Unity", "ECS", "Netcode"],
        "step_label": None,
        "bundle_id": None,
        "media": {"type": "video", "src": "../assets/videos/extractionz.mp4", "poster": "../assets/images/projects/extractionz.jpg"},
        "body_fr": """<p>Extraction Z est un FPS compétitif en 3v3 où deux équipes s'affrontent dans un environnement hostile peuplé de mutants. L'objectif est de localiser un artefact et de le ramener à sa base, tout en survivant aux hordes de zombies et aux assauts de l'équipe adverse.</p>
<p>Ce projet a représenté un défi technique majeur, réalisé par une équipe de seulement trois développeurs. Ce fut une opportunité d'apprentissage intensive, nous plongeant dans les nouvelles technologies d'Unity comme l'ECS (Entity Component System) et Netcode for Entities avec une expérience réseau limitée au départ. Ce challenge s'est avéré extrêmement enrichissant.</p>
<h4>Ma Contribution</h4>
<ul>
  <li><strong>Contrôleur FPS Avancé :</strong> Développement d'un contrôleur de personnage à la première personne avec une physique de joueur complexe.</li>
  <li><strong>Contrôleur de Caméra :</strong> Création d'un système de caméra avancé pour une expérience de jeu fluide et immersive.</li>
  <li><strong>Full Body Awareness :</strong> Implémentation d'un système de conscience corporelle complète personnalisé via des animations procédurales.</li>
  <li><strong>Gestion des Armes :</strong> Conception du système de gestion des armes, incluant la mécanique de tir.</li>
  <li><strong>Synchronisation Réseau :</strong> Prise en charge de la synchronisation des mouvements du joueur, des tirs et des effets visuels (VFX) avec Netcode for Entities.</li>
</ul>""",
        "body_en": """<p>Extraction Z is a competitive 3v3 FPS where two teams clash in a hostile, mutant-infested environment. The objective is to locate an artifact and bring it back to your base, all while surviving zombie hordes and fighting off the enemy team.</p>
<p>This project was a major technical challenge, undertaken by a team of just three developers. It was an intensive learning opportunity, diving into new Unity technologies like ECS (Entity Component System) and Netcode for Entities with limited prior networking experience. This challenge proved to be extremely rewarding.</p>
<h4>My Contribution</h4>
<ul>
  <li><strong>Advanced FPS Controller:</strong> Developed a first-person controller with complex player physics.</li>
  <li><strong>Advanced Camera Controller:</strong> Created an advanced camera system for a smooth and immersive gameplay experience.</li>
  <li><strong>Custom Full Body Awareness:</strong> Implemented a custom full body awareness system using procedural animation.</li>
  <li><strong>Weapon Management:</strong> Designed the weapon handling system, including shooting mechanics.</li>
  <li><strong>Network Synchronization:</strong> Handled the synchronization of player movements, shots, and visual effects (VFX) using Netcode for Entities.</li>
</ul>""",
    },
    {
        "slug": "iron-diver",
        "title_fr": "Iron Diver",
        "title_en": "Iron Diver",
        "subtitle_fr": "Jeu d'exploration 2D avec combats et gestion de boutique.",
        "subtitle_en": "2D exploration game with battles and shop management.",
        "year": "2024",
        "status_badge_type": "duration",
        "status_badge_fr": "8 semaines",
        "status_badge_en": "8 weeks",
        "people_fr": "10 personnes",
        "people_en": "10 persons",
        "role_fr": "Gameplay / Systèmes",
        "role_en": "Gameplay / Systems",
        "tags": ["C++", "SFML"],
        "stack": ["C++", "SFML"],
        "step_label": None,
        "bundle_id": None,
        "media": {"type": "video", "src": "../assets/videos/irondiver.mp4", "poster": "../assets/images/projects/irondiver.png"},
        "body_fr": """<p>Iron Diver est un jeu d'aventure immersif où vous incarnez un astronaute échoué sur une planète inconnue. Pour survivre, vous devez construire et piloter un petit robot, explorer un environnement captivant, collecter des ressources et les échanger avec les habitants locaux.</p>
<h4>Ma Contribution</h4>
<ul>
  <li><strong>Système de Craft :</strong> Développement du système de fabrication d'objets et d'améliorations.</li>
  <li><strong>Gestion de la Boutique :</strong> Conception et implémentation du système d'achat, de vente et d'échange de ressources avec les PNJ.</li>
  <li><strong>Gestion des Boosts :</strong> Développement de la logique pour les améliorations et capacités temporaires du robot.</li>
  <li><strong>Gestion des PNJ (Invités) :</strong> Programmation du comportement des habitants et de leurs interactions avec le joueur.</li>
  <li><strong>Gestion des Sauvegardes :</strong> Création du système de sauvegarde et de chargement de la progression du joueur.</li>
</ul>""",
        "body_en": """<p>Iron Diver is an immersive adventure game where you play as an astronaut stranded on a mysterious planet. To survive, you must build and control a small robot, explore a captivating environment, collect resources, and trade them with local inhabitants.</p>
<h4>My Contribution</h4>
<ul>
  <li><strong>Crafting System:</strong> Development of the item and upgrade crafting system.</li>
  <li><strong>Shop Management:</strong> Designed and implemented the system for buying, selling, and trading resources with NPCs.</li>
  <li><strong>Boost Management:</strong> Developed the logic for the robot's temporary upgrades and abilities.</li>
  <li><strong>Guest (NPC) Management:</strong> Programmed the behavior of the inhabitants and their interactions with the player.</li>
  <li><strong>Save Management:</strong> Created the system for saving and loading the player's progress.</li>
</ul>""",
    },
    {
        "slug": "dungeonscape",
        "title_fr": "DungeonScape",
        "title_en": "DungeonScape",
        "subtitle_fr": "Jeu de cartes et d'exploration de donjon en 2D, développé en C++ avec SFML.",
        "subtitle_en": "2D dungeon-crawling card game developed in C++ with the SFML library.",
        "year": "2024",
        "status_badge_type": "duration",
        "status_badge_fr": "8 semaines",
        "status_badge_en": "8 weeks",
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Développeur solo",
        "role_en": "Solo developer",
        "tags": ["C++", "SFML"],
        "stack": ["C++", "SFML"],
        "step_label": None,
        "bundle_id": None,
        "media": {"type": "video", "src": "../assets/videos/dungeonscape.mp4", "poster": "../assets/images/projects/dungeonscape.png"},
        "body_fr": """<p>Dungeonscape est un jeu de cartes et d'exploration de donjon en 2D, développé en C++ avec la bibliothèque SFML. Dans ce jeu au tour par tour, les joueurs choisissent parmi quatre héros, chacun avec des capacités uniques, pour s'aventurer dans un donjon.</p>
<h4>Ma Contribution</h4>
<ul>
  <li><strong>Gestion des Cartes :</strong> Implémentation de la logique pour piocher, jouer et défausser les cartes.</li>
  <li><strong>Gestion du Deck :</strong> Développement du système permettant aux joueurs de construire et gérer leur deck.</li>
  <li><strong>Interface Utilisateur (UI) :</strong> Création des éléments d'interface en jeu, comme la main du joueur, les points de vie et le chronomètre.</li>
</ul>""",
        "body_en": """<p>Dungeonscape is a 2D dungeon-crawling card game developed in C++ with the SFML library. In this turn-based game, players choose from four distinct heroes, each with unique abilities, to venture into a dungeon.</p>
<h4>My Contribution</h4>
<ul>
  <li><strong>Card Management:</strong> Implemented the logic for drawing, playing, and discarding cards.</li>
  <li><strong>Deck Management:</strong> Developed the system allowing players to build and manage their deck.</li>
  <li><strong>In-Game UI:</strong> Created the in-game interface elements, such as the player's hand, health points, and the timer.</li>
</ul>""",
    },
    {
        "slug": "game-launcher",
        "title_fr": "Game Launcher",
        "title_en": "Game Launcher",
        "subtitle_fr": "Lanceur de jeux développé en C# avec WPF — distribution et gestion de jeux automatisée.",
        "subtitle_en": "Game launcher developed in C# with WPF — automated game distribution and management.",
        "year": "2023",
        "status_badge": None,
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Développeur solo",
        "role_en": "Solo developer",
        "tags": ["C#", "WPF"],
        "stack": ["C#", "WPF", ".NET"],
        "step_label": None,
        "bundle_id": None,
        "media": {"type": "video", "src": "../assets/videos/launcher.mp4", "poster": "../assets/images/projects/launcher.png"},
        "body_fr": """<p>Ce lanceur de jeux, développé en C# avec WPF, est une solution complète pour la distribution et la gestion de jeux. Il automatise le téléchargement et l'installation des jeux depuis un serveur distant, tout en optimisant le processus grâce à un système de vérification de fichiers intelligent.</p>
<h4>Fonctionnalités Clés</h4>
<ul>
  <li><strong>Gestion des Fichiers :</strong> Télécharge, installe et vérifie automatiquement les fichiers du jeu par rapport à un manifeste distant.</li>
  <li><strong>Interface Utilisateur :</strong> Affiche les dernières actualités du jeu et une barre de progression visuelle.</li>
  <li><strong>Intégration Système :</strong> Discord Rich Presence, minimisation dans la barre des tâches, menu contextuel.</li>
  <li><strong>Paramètres :</strong> Raccourcis vers le dossier du jeu, site web, Discord, et option de lancement au démarrage Windows.</li>
</ul>""",
        "body_en": """<p>This game launcher, developed in C# with WPF, is a complete solution for game distribution and management. It automates the download and installation of games from a remote server with a smart file verification system.</p>
<h4>Key Features</h4>
<ul>
  <li><strong>File Management:</strong> Automatically downloads, installs, and verifies game files against a remote manifest.</li>
  <li><strong>User Interface:</strong> Displays the latest game news and a visual progress bar to track downloads.</li>
  <li><strong>System Integration:</strong> Discord Rich Presence, system tray support, context menu for quick actions.</li>
  <li><strong>Settings:</strong> Shortcuts to open the game folder, website, Discord, and a Windows startup option.</li>
</ul>""",
    },
    {
        "slug": "ullo-prototype",
        "title_fr": "Prototype de Jeu - Stage",
        "title_en": "Game Prototype - Intern",
        "subtitle_fr": "Prototype développé lors d'un stage chez Ullo — jeu exploitant le neurofeedback en VR.",
        "subtitle_en": "Prototype developed during internship at Ullo — neurofeedback-based VR game.",
        "year": "2021",
        "status_badge": None,
        "people_fr": "1 personne",
        "people_en": "1 person",
        "role_fr": "Stagiaire Unity",
        "role_en": "Unity intern",
        "tags": ["C#", "Unity", "VR"],
        "stack": ["C#", "Unity", "VR", "Muse"],
        "step_label": None,
        "bundle_id": None,
        "media": {"type": "image", "src": "../assets/images/projects/proto.png"},
        "body_fr": """<p>Ce projet a été réalisé sur Unity durant mon stage de 5 semaines au sein de l'entreprise Ullo. C'est un jeu exploitant le neurofeedback (modulation de l'activité cérébrale) en combinant un Oculus Quest, un bandeau Muse pour l'activité cérébrale, et une montre connectée pour le rythme respiratoire.</p>
<h4>Fonctionnalités Implémentées</h4>
<ul>
  <li><strong>Gameplay basé sur le Neurofeedback :</strong> La capacité de voler est directement liée aux fréquences cérébrales du joueur.</li>
  <li><strong>Création d'Environnement :</strong> Mise en place du monde de jeu avec terrain, ciel personnalisable et plateformes.</li>
  <li><strong>Interaction Dynamique :</strong> Les objets du jeu changent de position et de forme en fonction des données de neurofeedback.</li>
  <li><strong>Système de Collectibles :</strong> Intégration de pièces à récupérer avec un compteur de score.</li>
  <li><strong>Interface Utilisateur :</strong> Création d'une UI permettant de configurer différents paramètres du jeu.</li>
</ul>""",
        "body_en": """<p>This project was developed in Unity during my 5-week internship at Ullo. It uses neurofeedback (brain activity modulation) combining an Oculus Quest, a Muse headband, and a smartwatch.</p>
<h4>Implemented Features</h4>
<ul>
  <li><strong>Neurofeedback-Based Gameplay:</strong> The ability to fly is directly linked to the player's brain frequencies.</li>
  <li><strong>Environment Creation:</strong> Game world with terrain, customizable sky, and platforms.</li>
  <li><strong>Dynamic Interaction:</strong> Game objects change position and shape based on neurofeedback data.</li>
  <li><strong>Collectible System:</strong> Coins with a score counter.</li>
  <li><strong>User Interface:</strong> UI to configure various game settings.</li>
</ul>""",
    },
]

# Bundle definitions
BUNDLES = {
    "multiplayer-ecosystem": {
        "name_fr": "Écosystème Multijoueur",
        "name_en": "Multiplayer Ecosystem",
        "num": "bundle_01",
        "steps": [
            ("lkz-network", "LKZ Network", "step_01 // engine"),
            ("lkz-online-services", "LKZ Online Services", "step_02 // services"),
            ("dead-protocol", "Dead Protocol", "step_03 // game"),
        ],
    },
    "heist-day": {
        "name_fr": "Heist Day",
        "name_en": "Heist Day",
        "num": "bundle_02",
        "steps": [
            ("heist-day-matchmaker", "heist-day-matchmaker", "step_01 // backend"),
            ("heist-day", "Heist Day", "step_02 // game"),
        ],
    },
}

# Flat list for prev/next navigation
PROJECT_ORDER = [p["slug"] for p in PROJECTS]
PROJECT_BY_SLUG = {p["slug"]: p for p in PROJECTS}


def build_badges(p):
    """Return HTML for badges."""
    badges = [f'<span class="badge date-badge">{p["year"]}</span>']
    if p.get("status_badge") == "WIP":
        badges.append('<span class="badge wip-badge">WIP</span>')
    elif p.get("status_badge_type") == "duration":
        badges.append(
            f'<span class="badge duration-badge" '
            f'data-lang-fr="{p["status_badge_fr"]}" data-lang-en="{p["status_badge_en"]}">{p["status_badge_fr"]}</span>'
        )
    return "\n          ".join(badges)


def build_tags(tags):
    return "".join(f'<span class="tag">{t}</span>' for t in tags)


def build_stack_list(stack):
    return "".join(f"<span>{s}</span>" for s in stack)


def build_media(media):
    t = media["type"]
    if t == "video":
        poster_attr = f' poster="{media["poster"]}"' if media.get("poster") else ""
        return f'<video src="{media["src"]}" controls muted loop playsinline{poster_attr}></video>'
    elif t == "image":
        return f'<img src="{media["src"]}" alt="">'
    else:  # placeholder
        return f'<div class="card-img-placeholder"><span class="placeholder-icon">{media["src"]}</span></div>'


def build_chain(p):
    """Build the story-chain sidebar for bundled projects."""
    if not p.get("bundle_id"):
        return ""
    bundle = BUNDLES[p["bundle_id"]]
    items = []
    for i, (slug, title, step) in enumerate(bundle["steps"], start=1):
        classes = "pd-chain-item"
        href = f'{slug}.html'
        if slug == p["slug"]:
            classes += " current"
            # current item: still a span, not a link
            items.append(
                f'''<div class="{classes}">
            <div class="pd-chain-num">{i:02d}</div>
            <div class="pd-chain-body">
              <div class="pd-chain-title">{title}</div>
              <span class="pd-chain-step">{step}</span>
            </div>
          </div>'''
            )
        else:
            items.append(
                f'''<a class="{classes}" href="{href}">
            <div class="pd-chain-num">{i:02d}</div>
            <div class="pd-chain-body">
              <div class="pd-chain-title">{title}</div>
              <span class="pd-chain-step">{step}</span>
            </div>
          </a>'''
            )
    return f'''
        <div class="pd-chain">
          <h5 data-lang-fr="// Parcours du Bundle" data-lang-en="// Bundle Journey">// Parcours du Bundle</h5>
          {chr(10).join(items)}
        </div>'''


def build_prev_next(slug):
    idx = PROJECT_ORDER.index(slug)
    prev_html = ""
    next_html = ""
    if idx > 0:
        prev = PROJECT_BY_SLUG[PROJECT_ORDER[idx - 1]]
        prev_html = f'''<a class="pd-nav-btn pd-nav-back" href="{prev["slug"]}.html">
          <span class="pd-nav-dir" data-lang-fr="← Projet précédent" data-lang-en="← Previous project">← Projet précédent</span>
          <span class="pd-nav-title" data-lang-fr="{prev["title_fr"]}" data-lang-en="{prev["title_en"]}">{prev["title_fr"]}</span>
        </a>'''
    else:
        prev_html = '<span></span>'
    if idx < len(PROJECT_ORDER) - 1:
        nxt = PROJECT_BY_SLUG[PROJECT_ORDER[idx + 1]]
        next_html = f'''<a class="pd-nav-btn pd-nav-next" href="{nxt["slug"]}.html">
          <span class="pd-nav-dir" data-lang-fr="Projet suivant →" data-lang-en="Next project →">Projet suivant →</span>
          <span class="pd-nav-title" data-lang-fr="{nxt["title_fr"]}" data-lang-en="{nxt["title_en"]}">{nxt["title_fr"]}</span>
        </a>'''
    else:
        next_html = '<span></span>'
    return prev_html, next_html


def build_bundle_breadcrumb(p):
    if not p.get("bundle_id"):
        return ""
    bundle = BUNDLES[p["bundle_id"]]
    return f'''<a href="../index.html#projects" data-lang-fr="{bundle["name_fr"]}" data-lang-en="{bundle["name_en"]}">{bundle["name_fr"]}</a>
      <span class="pd-sep">/</span>
      '''


def build_page(p):
    badges_html = build_badges(p)
    tags_html = build_tags(p["tags"])
    stack_html = build_stack_list(p["stack"])
    media_html = build_media(p["media"])
    chain_html = build_chain(p)
    prev_html, next_html = build_prev_next(p["slug"])
    bundle_crumb = build_bundle_breadcrumb(p)

    step_label_html = ""
    if p.get("step_label"):
        step_label_html = f'<span class="bundle-step" style="margin-bottom: 14px;">{p["step_label"]}</span>'

    title = p["title_fr"]
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Mateo Scarpetta</title>
  <meta name="description" content="{p["subtitle_fr"]}">
  <link rel="stylesheet" href="../style/style.css" />
</head>
<body class="project-page">
  <header>
    <div class="container">
      <a href="../index.html#about" class="nav-logo">
        <span class="logo-bracket">&lt;</span>MS<span class="logo-slash"> /</span><span class="logo-bracket">&gt;</span>
      </a>

      <button id="menu-toggle" class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="main-nav">
        <span></span><span></span><span></span>
      </button>

      <nav id="main-nav">
        <a href="../index.html#about"><span class="nav-num">01.</span><span data-lang-fr="À propos" data-lang-en="About">À propos</span></a>
        <a href="../index.html#projects"><span class="nav-num">02.</span><span data-lang-fr="Projets" data-lang-en="Projects">Projets</span></a>
        <a href="../index.html#skills"><span class="nav-num">03.</span><span data-lang-fr="Compétences" data-lang-en="Skills">Compétences</span></a>
        <a href="../index.html#experience"><span class="nav-num">04.</span><span data-lang-fr="Parcours" data-lang-en="Experience">Parcours</span></a>
        <a href="../index.html#contact"><span class="nav-num">05.</span><span data-lang-fr="Contact" data-lang-en="Contact">Contact</span></a>
        <div class="mobile-only-container"></div>
      </nav>

      <div class="header-right">
        <div class="lang-toggle" aria-label="Switch language" role="button">
          <span class="lang-option">FR</span>
          <span class="lang-option">EN</span>
          <span class="lang-slider"></span>
        </div>
        <div class="social-icons">
          <a href="https://github.com/leikyz" target="_blank" title="GitHub">
            <img src="../assets/images/icon/github.png" alt="GitHub Icon">
          </a>
          <a href="https://www.linkedin.com/in/mateo-scarpetta-79a89328b" target="_blank" title="LinkedIn">
            <img src="../assets/images/icon/linkedin.png" alt="LinkedIn Icon">
          </a>
          <a href="../assets/FR_CV_MATEO_SCARPETTA.pdf" target="_blank" title="CV" class="cv-link" data-cv-fr="../assets/FR_CV_MATEO_SCARPETTA.pdf" data-cv-en="../assets/EN_CV_MATEO_SCARPETTA.pdf">
            <img src="../assets/images/icon/cv.png" alt="CV Icon" class="cv-icon-img">
          </a>
          <a href="mailto:leikyz17@outlook.com" title="Email">
            <img src="../assets/images/icon/email.png" alt="Mail Icon">
          </a>
        </div>
      </div>
    </div>
  </header>

  <main>
    <!-- Breadcrumb -->
    <div class="pd-breadcrumb">
      <a href="../index.html#projects" data-lang-fr="← Projets" data-lang-en="← Projects">← Projets</a>
      <span class="pd-sep">/</span>
      {bundle_crumb}<span class="pd-current" data-lang-fr="{p["title_fr"]}" data-lang-en="{p["title_en"]}">{p["title_fr"]}</span>
    </div>

    <!-- Hero -->
    <div class="pd-hero">
      <div class="pd-hero-meta">
        <span class="pd-hero-id">// project_{p["slug"].replace("-", "_")}</span>
        <div class="pd-hero-badges">
          {badges_html}
        </div>
      </div>
      {step_label_html}
      <h1 data-lang-fr="{p["title_fr"]}" data-lang-en="{p["title_en"]}">{p["title_fr"]}</h1>
      <p class="pd-hero-subtitle"
         data-lang-fr="{p["subtitle_fr"]}"
         data-lang-en="{p["subtitle_en"]}">{p["subtitle_fr"]}</p>
      <div class="pd-hero-tags project-tags">
        {tags_html}
      </div>
    </div>

    <!-- Media -->
    <div class="pd-media">
      {media_html}
    </div>

    <!-- Content + Sidebar -->
    <div class="pd-layout">
      <div class="pd-content">
        <div data-lang-content-fr>{p["body_fr"]}</div>
        <div data-lang-content-en style="display:none">{p["body_en"]}</div>
      </div>

      <aside class="pd-sidebar">
        <div class="pd-info-card">
          <h5 data-lang-fr="// Informations" data-lang-en="// Information">// Informations</h5>
          <div class="pd-info-row">
            <span class="pd-info-label" data-lang-fr="Année" data-lang-en="Year">Année</span>
            <span class="pd-info-value">{p["year"]}</span>
          </div>
          <div class="pd-info-row">
            <span class="pd-info-label" data-lang-fr="Équipe" data-lang-en="Team">Équipe</span>
            <span class="pd-info-value" data-lang-fr="{p["people_fr"]}" data-lang-en="{p["people_en"]}">{p["people_fr"]}</span>
          </div>
          <div class="pd-info-row">
            <span class="pd-info-label" data-lang-fr="Rôle" data-lang-en="Role">Rôle</span>
            <span class="pd-info-value" data-lang-fr="{p["role_fr"]}" data-lang-en="{p["role_en"]}">{p["role_fr"]}</span>
          </div>
        </div>

        <div class="pd-info-card">
          <h5 data-lang-fr="// Stack Technique" data-lang-en="// Tech Stack">// Stack Technique</h5>
          <div class="pd-stack-list">
            {stack_html}
          </div>
        </div>
        {chain_html}
      </aside>
    </div>

    <!-- Prev/Next -->
    <div class="pd-nav-footer">
      {prev_html}
      {next_html}
    </div>
  </main>

  <!-- Back to Top Button -->
  <a href="#" class="back-to-top" title="Retour en haut" data-lang-fr-title="Retour en haut" data-lang-en-title="Back to top">&#8679;</a>

  <!-- Shared page logic -->
  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      // Responsive menu
      const menuToggle = document.getElementById('menu-toggle');
      const mainNav = document.getElementById('main-nav');
      const mobileOnlyContainer = document.querySelector('.mobile-only-container');
      if (mobileOnlyContainer) {{
        const socialIcons = document.querySelector('header .social-icons').cloneNode(true);
        const langToggle = document.querySelector('header .lang-toggle').cloneNode(true);
        mobileOnlyContainer.appendChild(langToggle);
        mobileOnlyContainer.appendChild(socialIcons);
      }}
      menuToggle.addEventListener('click', function () {{
        const isActive = mainNav.classList.toggle('active');
        this.setAttribute('aria-expanded', isActive);
      }});
      mainNav.addEventListener('click', (e) => {{
        if (e.target.closest('a') && !e.target.closest('.lang-toggle')) {{
          mainNav.classList.remove('active');
          menuToggle.setAttribute('aria-expanded', 'false');
        }}
      }});

      // Language switcher (matches index.html conventions)
      const translatableElements = document.querySelectorAll('[data-lang-fr], [data-lang-en]');
      const cvLinks = document.querySelectorAll('.cv-link');
      const langToggles = document.querySelectorAll('.lang-toggle');

      const setLanguage = (lang) => {{
        const key = 'lang' + lang.charAt(0).toUpperCase() + lang.slice(1);
        translatableElements.forEach(el => {{
          if (el.dataset[key] !== undefined) {{
            el.innerHTML = el.dataset[key];
          }}
          if (el.dataset[key + 'Title']) {{
            el.title = el.dataset[key + 'Title'];
          }}
        }});

        // Language-specific body content blocks
        document.querySelectorAll('[data-lang-content-fr]').forEach(el => {{
          el.style.display = lang === 'fr' ? '' : 'none';
        }});
        document.querySelectorAll('[data-lang-content-en]').forEach(el => {{
          el.style.display = lang === 'en' ? '' : 'none';
        }});

        // CV links (mirrors index.html exact code, including its existing quirks)
        cvLinks.forEach(link => {{
          const cvPath = link.dataset['cv' + lang];
          if (cvPath) link.href = cvPath;
        }});

        document.documentElement.lang = lang;
        try {{ localStorage.setItem('language', lang); }} catch(e) {{}}

        langToggles.forEach(toggle => {{
          if (lang === 'fr') toggle.classList.add('lang-fr');
          else toggle.classList.remove('lang-fr');
        }});
      }};

      document.body.addEventListener('click', function(e) {{
        if (e.target.closest('.lang-toggle')) {{
          const currentLang = localStorage.getItem('language') || 'en';
          setLanguage(currentLang === 'fr' ? 'en' : 'fr');
        }}
      }});

      const initialLang = (function() {{ try {{ return localStorage.getItem('language'); }} catch(e) {{ return null; }} }})() || 'fr';
      setLanguage(initialLang);

      // Back to top button
      const backToTopButton = document.querySelector(".back-to-top");
      window.addEventListener("scroll", () => {{
        if (window.scrollY > 300) backToTopButton.classList.add("visible");
        else backToTopButton.classList.remove("visible");
      }});
    }});
  </script>
</body>
</html>
'''
    return html


for p in PROJECTS:
    html = build_page(p)
    with open(os.path.join(OUTPUT_DIR, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote projects/{p['slug']}.html  ({len(html)} chars)")

print(f"\n✅ {len(PROJECTS)} project pages generated.")
