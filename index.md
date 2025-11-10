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

.topic-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  background: #fafafa;
}

.topic-card h3 {
  margin-top: 0;
  color: #2196F3;
}

.topic-meta {
  color: #666;
  font-size: 14px;
  margin: 10px 0;
}

.topic-links {
  margin-top: 15px;
}

.topic-links a {
  display: inline-block;
  margin-right: 15px;
  text-decoration: none;
  color: #2196F3;
  font-weight: 500;
}

.topic-links a:hover {
  text-decoration: underline;
}
</style>

<div class="tabs">
  <button class="tab-button active" onclick="openTab(event, 'grammatik')">📖 Grammatik</button>
  <button class="tab-button" onclick="openTab(event, 'vokabular')">📚 Vokabular</button>
  <button class="tab-button" onclick="openTab(event, 'info')">ℹ️ Info</button>
</div>

<div id="grammatik" class="tab-content active">

## Grammatikthemen

<div class="topic-card">

### 01. Vergangenheitsformen: Perfekt und Plusquamperfekt

Eine umfassende Anleitung zur Bildung und Verwendung von Perfekt und Plusquamperfekt. Inkl. Konjugationstabellen und häufigen unregelmäßigen Verben.

<div class="topic-meta">
<strong>Themen:</strong> Perfekt, Plusquamperfekt, Partizip II, haben/sein<br>
<strong>Niveau:</strong> B2-C1
</div>

<div class="topic-links">
📚 <a href="grammatik/01_vergangenheitsformen/erklaerung.md">Zur Lektion</a>
✏️ <a href="grammatik/01_vergangenheitsformen/aufgaben.md">Übungen</a>
</div>

</div>

<a href="grammatik/" style="display: inline-block; margin-top: 20px; color: #2196F3; font-weight: 500;">→ Alle Grammatikthemen anzeigen</a>

</div>

<div id="vokabular" class="tab-content">

## Vokabelthemen

<div class="topic-card">

### 01. Essen und Küche

Umfangreiches Vokabular rund um Essen, Kochen und Küche. Von Küchengeräten bis zu Gewürzen.

<div class="topic-meta">
<strong>Wörter:</strong> 50+ Vokabeln<br>
<strong>Kategorien:</strong> Küchengeräte, Mahlzeiten, Gewürze, Verben
</div>

<div class="topic-links">
📝 <a href="vokabular/01_essen/">Vokabelliste ansehen</a>
</div>

</div>

<a href="vokabular/" style="display: inline-block; margin-top: 20px; color: #2196F3; font-weight: 500;">→ Alle Vokabelthemen anzeigen</a>

</div>

<div id="info" class="tab-content">

## Über dieses Projekt

Diese Lernplattform ist mein persönliches Tool zur Vorbereitung auf das C1-Zertifikat in Deutsch. Alle Inhalte werden kontinuierlich erweitert und verbessert.

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
