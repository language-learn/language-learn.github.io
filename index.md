# Deutsch C1 Lernplattform

Willkommen auf meiner persönlichen Lernplattform für die deutsche Sprache! Hier dokumentiere ich meinen Weg zum C1-Zertifikat mit strukturierten Vokabeln, Grammatikerklärungen und Übungen.

<style>
.tabs {
  display: flex;
  border-bottom: 2px solid #e0e0e0;
  margin-bottom: 30px;
  gap: 10px;
}

.tab-button {
  padding: 12px 24px;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  color: #666;
  border-bottom: 3px solid transparent;
  transition: all 0.3s;
}

.tab-button:hover {
  color: #000;
  background: #f5f5f5;
}

.tab-button.active {
  color: #2196F3;
  border-bottom-color: #2196F3;
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.topic-list {
  list-style: none;
  padding: 0;
}

.topic-list li {
  margin: 15px 0;
  padding: 15px;
  border-left: 3px solid #2196F3;
  background: #f9f9f9;
}

.topic-list li a {
  color: #2196F3;
  font-weight: 500;
  font-size: 18px;
  text-decoration: none;
}

.topic-list li a:hover {
  text-decoration: underline;
}

.topic-list li .topic-desc {
  color: #666;
  font-size: 14px;
  margin-top: 5px;
}

.intro-text {
  color: #666;
  margin-bottom: 25px;
  line-height: 1.6;
}
</style>

<div class="tabs">
  <button class="tab-button active" onclick="openTab(event, 'grammatik')">📖 Grammatik</button>
  <button class="tab-button" onclick="openTab(event, 'vokabular')">📚 Vokabular</button>
  <button class="tab-button" onclick="openTab(event, 'info')">ℹ️ Info</button>
</div>

<div id="grammatik" class="tab-content active">

## Grammatik

<p class="intro-text">
Auf dieser Seite findest du systematische Erklärungen deutscher Grammatikregeln mit Beispielen und Übungen für das C1-Niveau. Jedes Thema enthält ausführliche Erklärungen und praktische Übungen.
</p>

### Verfügbare Themen:

<ul class="topic-list">
  <li>
    <a href="grammatik/01_vergangenheitsformen/erklaerung.md">01. Vergangenheitsformen (Perfekt & Plusquamperfekt)</a>
    <div class="topic-desc">Bildung und Verwendung von Perfekt und Plusquamperfekt • Niveau: B2-C1</div>
  </li>
</ul>

</div>

<div id="vokabular" class="tab-content">

## Vokabular

<p class="intro-text">
Hier findest du thematisch organisierte Vokabellisten mit deutschen Wörtern und englischen Übersetzungen. Alle Übersetzungen wurden mit professionellen Tools erstellt und sind nach Themen sortiert.
</p>

### Verfügbare Themen:

<ul class="topic-list">
  <li>
    <a href="vokabular/01_essen/">01. Essen und Küche</a>
    <div class="topic-desc">Besteck, Küchengeräte, Mahlzeiten, Gewürze und Koch-Verben • 50+ Vokabeln</div>
  </li>
</ul>

</div>

<div id="info" class="tab-content">

## Info

<p class="intro-text">
Diese Lernplattform ist mein persönliches Tool zur Vorbereitung auf das C1-Zertifikat in Deutsch. Alle Inhalte werden kontinuierlich erweitert und verbessert.
</p>

### Lernmethode

1. **Grammatik verstehen** - Regeln lernen und internalisieren
2. **Vokabular aufbauen** - Thematische Wortschatzarbeit
3. **Üben, üben, üben** - Regelmäßige Übungen und Anwendung

### Struktur

- **Grammatik**: Systematische Erklärungen deutscher Grammatikregeln mit Beispielen und Übungen
- **Vokabular**: Thematisch organisierte Vokabellisten mit deutschen Wörtern und englischen Übersetzungen

---

*Letzte Aktualisierung: November 2025*

</div>

<script>
function openTab(evt, tabName) {
  // Hide all tab contents
  var tabContents = document.getElementsByClassName("tab-content");
  for (var i = 0; i < tabContents.length; i++) {
    tabContents[i].classList.remove("active");
  }

  // Remove active class from all buttons
  var tabButtons = document.getElementsByClassName("tab-button");
  for (var i = 0; i < tabButtons.length; i++) {
    tabButtons[i].classList.remove("active");
  }

  // Show the selected tab and mark button as active
  document.getElementById(tabName).classList.add("active");
  evt.currentTarget.classList.add("active");
}
</script>
