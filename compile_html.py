import os

# Read the base64 string
base64_path = '/Users/catherinetseng/.gemini/antigravity/scratch/jelly_base64.txt'
with open(base64_path, 'r') as f:
    jelly_base64 = f.read().strip()

# Prepare the HTML contents
html_template = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>小小資安與健康生活守護者</title>
  
  <!-- PWA Manifest -->
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#4A90E2">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="小小資安與健康生活守護者">
  <link rel="apple-touch-icon" href="jelly_person.png">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-color: #FFFDF6;
      --border-color: #3D362A;
      --primary-blue: #B1D4EC;
      --primary-blue-dark: #4D7EAB;
      --primary-orange: #F3C19C;
      --primary-orange-dark: #C67844;
      --primary-pink: #F6C4C8;
      --primary-red: #F2A1A1;
      --primary-red-dark: #C36161;
      --primary-green: #A7DCA8;
      --primary-green-dark: #4F9151;
      --font-primary: 'Outfit', 'Noto Sans TC', sans-serif;
      --app-scale: 1;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      width: 100vw;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: #EAE3C9;
      font-family: var(--font-primary);
      overflow: hidden;
      user-select: none;
      -webkit-user-select: none;
    }

    /* Container lock to 1280x800 */
    #app-container {
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%) scale(var(--app-scale, 1));
      transform-origin: center center;
      width: 1280px;
      height: 800px;
      background: var(--bg-color);
      border-radius: 24px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      border: 6px solid var(--border-color);
    }

    /* Global Typography & Elements */
    h1, h2, h3, p, button, span {
      color: var(--border-color);
    }

    h1 {
      font-size: 36px;
      font-weight: 900;
    }

    h2 {
      font-size: 28px;
      font-weight: 700;
    }

    p, span, div {
      font-size: 18px;
      font-weight: 700;
      line-height: 1.5;
    }

    button {
      font-family: var(--font-primary);
      font-size: 18px;
      font-weight: 800;
      height: 48px;
      padding: 0 24px;
      border: 3px solid var(--border-color);
      border-radius: 16px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      box-shadow: 4px 4px 0px var(--border-color);
      transition: transform 0.1s, box-shadow 0.1s;
      outline: none;
    }

    button:active {
      transform: translate(3px, 3px);
      box-shadow: 1px 1px 0px var(--border-color);
    }

    /* Top Navigation / Status Bar */
    #top-bar {
      height: 80px;
      width: 100%;
      border-bottom: 5px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 30px;
      background: #FFFFFF;
      z-index: 10;
    }

    .top-bar-title {
      font-size: 24px;
      font-weight: 900;
    }

    .timer-container {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 16px;
      background: var(--primary-pink);
      border: 3px solid var(--border-color);
      border-radius: 12px;
      box-shadow: 2px 2px 0px var(--border-color);
    }

    .timer-text {
      font-size: 20px;
      font-weight: 900;
      font-variant-numeric: tabular-nums;
    }

    .timer-flash {
      animation: flash-red 0.5s infinite alternate;
      border-color: var(--primary-red-dark);
      background-color: var(--primary-red);
    }

    @keyframes flash-red {
      0% {
        opacity: 1;
        box-shadow: 0 0 4px var(--primary-red-dark);
      }
      100% {
        opacity: 0.7;
        box-shadow: 0 0 15px var(--primary-red-dark);
      }
    }

    .btn-back {
      background: #FFFFFF;
    }
    .btn-back:hover {
      background: var(--bg-color);
    }

    /* Views System */
    .view {
      display: none;
      width: 100%;
      flex: 1;
      min-height: 0;
      overflow: hidden;
      position: relative;
    }

    .view.active {
      display: flex;
    }

    /* View: Home Screen */
    #view-home {
      flex-direction: column;
      align-items: center;
      padding: 40px;
      justify-content: space-between;
      background: radial-gradient(circle, #FFFDF6 60%, #FAF6EA 100%);
    }

    .home-header {
      text-align: center;
      margin-top: 10px;
    }

    .home-title {
      font-size: 44px;
      font-weight: 900;
      color: var(--primary-blue-dark);
      text-shadow: 2px 2px 0px var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-bottom: 8px;
    }

    .home-subtitle {
      font-size: 20px;
      color: #6C6251;
      font-weight: 600;
    }

    .games-grid {
      display: flex;
      gap: 24px;
      width: 100%;
      max-width: 900px;
      justify-content: center;
      margin: 30px 0;
    }

    .game-card {
      flex: 1;
      max-width: 280px;
      background: #FFFFFF;
      border: 4px solid var(--border-color);
      border-radius: 24px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      box-shadow: 6px 6px 0px var(--border-color);
      transition: transform 0.2s, box-shadow 0.2s;
      cursor: pointer;
      position: relative;
    }

    .game-card:hover {
      transform: translateY(-8px);
      box-shadow: 10px 10px 0px var(--border-color);
    }

    .game-card:active {
      transform: translateY(-2px);
      box-shadow: 4px 4px 0px var(--border-color);
    }

    .game-card-icon {
      font-size: 60px;
      margin-bottom: 15px;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 80px;
    }

    .game-card-title {
      font-size: 22px;
      font-weight: 900;
      margin-bottom: 12px;
    }

    .game-card-desc {
      font-size: 16px;
      color: #7A7060;
      font-weight: 600;
      line-height: 1.4;
      flex-grow: 1;
      margin-bottom: 20px;
    }

    .game-status-badge {
      font-size: 16px;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 20px;
      border: 2px solid var(--border-color);
      background-color: var(--primary-orange);
    }

    .game-status-badge.completed {
      background-color: var(--primary-green);
      color: var(--border-color);
    }

    .home-footer {
      display: flex;
      gap: 20px;
      align-items: center;
    }

    .btn-resetProgress {
      background: var(--primary-red);
      font-size: 16px;
      height: 40px;
    }

    .total-progress-bar-container {
      width: 300px;
      height: 24px;
      background: #FFFFFF;
      border: 3px solid var(--border-color);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 2px 2px 0px var(--border-color);
      display: flex;
      position: relative;
    }

    .total-progress-fill {
      height: 100%;
      background: var(--primary-green);
      width: 0%;
      transition: width 0.5s ease-in-out;
    }

    .total-progress-text {
      position: absolute;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: 900;
    }

    /* Global Gameplay Layout */
    .game-layout {
      display: flex;
      width: 100%;
      height: 100%;
      padding: 16px 20px 24px 20px;
      gap: 16px;
    }

    .game-left-panel {
      width: 320px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 20px;
      background: #FFFFFF;
      border: 4px solid var(--border-color);
      border-radius: 24px;
      box-shadow: 4px 4px 0px var(--border-color);
      padding: 20px;
      position: relative;
    }

    .jelly-avatar-container {
      width: 160px;
      height: 160px;
      border: 4px solid var(--border-color);
      border-radius: 80px;
      background: var(--primary-pink);
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      box-shadow: 3px 3px 0px var(--border-color);
      position: relative;
    }

    .jelly-avatar-img {
      width: 130px;
      height: 130px;
      object-fit: contain;
      transform-origin: bottom center;
      transition: filter 0.3s ease;
    }

    .jelly-avatar-img.bounce {
      animation: avatar-bounce 0.6s ease infinite alternate;
    }

    @keyframes avatar-bounce {
      0% { transform: translateY(0) scale(1); }
      100% { transform: translateY(-8px) scale(0.95, 1.05); }
    }

    .jelly-speech-bubble {
      background: var(--primary-blue);
      border: 3px solid var(--border-color);
      border-radius: 20px;
      padding: 16px;
      width: 100%;
      box-shadow: 3px 3px 0px var(--border-color);
      position: relative;
      min-height: 100px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .jelly-speech-bubble::before {
      content: '';
      position: absolute;
      bottom: -15px;
      left: 50%;
      transform: translateX(-50%);
      border-width: 15px 15px 0;
      border-style: solid;
      border-color: var(--border-color) transparent;
      display: block;
      width: 0;
    }

    .jelly-speech-bubble::after {
      content: '';
      position: absolute;
      bottom: -10px;
      left: 50%;
      transform: translateX(-50%);
      border-width: 12px 12px 0;
      border-style: solid;
      border-color: var(--primary-blue) transparent;
      display: block;
      width: 0;
    }

    .game-right-panel {
      flex: 1;
      background: #FFFFFF;
      border: 4px solid var(--border-color);
      border-radius: 24px;
      box-shadow: 4px 4px 0px var(--border-color);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }

    /* Start and End screens in game views */
    .game-screen {
      display: none;
      width: 100%;
      height: 100%;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px;
      position: absolute;
      top: 0;
      left: 0;
      background: var(--bg-color);
      z-index: 5;
    }

    .game-screen.active {
      display: flex;
    }

    .screen-title {
      font-size: 38px;
      font-weight: 900;
      margin-bottom: 24px;
      text-align: center;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .screen-subtitle {
      font-size: 22px;
      color: #6C6251;
      margin-bottom: 30px;
      text-align: center;
      max-width: 600px;
    }

    .btn-start-game {
      background: var(--primary-orange);
      font-size: 24px;
      height: 60px;
      padding: 0 40px;
      border-radius: 20px;
    }

    .btn-start-game:hover {
      background: var(--primary-orange-dark);
      color: #FFFFFF;
    }

    /* Game 1: 網路交友偵探 Elements */
    .game1-workspace {
      display: flex;
      flex-direction: column;
      height: 100%;
    }

    .game1-header {
      padding: 15px 20px;
      border-bottom: 3px solid var(--border-color);
      background: var(--primary-blue);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .game1-step-indicator {
      background: #FFFFFF;
      padding: 4px 12px;
      border: 2px solid var(--border-color);
      border-radius: 10px;
      font-size: 16px;
      font-weight: 800;
    }

    .game1-content {
      flex: 1;
      display: flex;
      overflow: hidden;
    }

    .chat-container {
      flex: 1.1;
      border-right: 3px solid var(--border-color);
      background: #F3EFE0;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 24px;
      overflow-y: auto;
    }

    .chat-bubble {
      max-width: 85%;
      padding: 12px 18px;
      border-radius: 18px;
      border: 3px solid var(--border-color);
      box-shadow: 2px 2px 0px var(--border-color);
      position: relative;
      animation: bubble-pop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    @keyframes bubble-pop {
      0% { transform: scale(0.8); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }

    .chat-bubble.stranger {
      align-self: flex-start;
      background: #FFFFFF;
      border-bottom-left-radius: 4px;
    }

    .chat-bubble.stranger::before {
      content: '網友';
      position: absolute;
      top: -22px;
      left: 5px;
      font-size: 12px;
      font-weight: 800;
      color: #7A7060;
    }

    /* Clickable secret sentence inside chat */
    .danger-phrase {
      display: inline-block;
      cursor: pointer;
      padding: 2px 6px;
      border-radius: 8px;
      background-color: transparent;
      border: 2px solid transparent;
      transition: background-color 0.2s, border-color 0.2s;
    }

    .danger-phrase:hover {
      background-color: rgba(61, 54, 42, 0.05);
      border: 2px dashed rgba(61, 54, 42, 0.15);
    }

    .danger-phrase.detected {
      background-color: var(--primary-red);
      border: 2px solid var(--primary-red-dark);
      animation: danger-pulse 0.8s infinite alternate;
      color: var(--border-color);
    }

    @keyframes danger-pulse {
      0% { box-shadow: 0 0 0px var(--primary-red-dark); }
      100% { box-shadow: 0 0 10px var(--primary-red-dark); }
    }

    .game1-right-panel {
      flex: 0.9;
      background: #FFFFFF;
      display: flex;
      flex-direction: column;
      padding: 20px;
      justify-content: center;
    }

    .mc-container {
      display: none;
      flex-direction: column;
      gap: 15px;
      height: 100%;
      justify-content: center;
      animation: slide-in 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .mc-container.active {
      display: flex;
    }

    .mc-question {
      font-size: 20px;
      font-weight: 900;
      margin-bottom: 10px;
      border-left: 5px solid var(--primary-orange-dark);
      padding-left: 10px;
    }

    .mc-options {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .mc-option {
      background: #FFFDF6;
      border: 3px solid var(--border-color);
      border-radius: 12px;
      padding: 12px 16px;
      font-size: 18px;
      font-weight: 700;
      text-align: left;
      cursor: pointer;
      box-shadow: 3px 3px 0px var(--border-color);
      transition: transform 0.1s, box-shadow 0.1s, background-color 0.2s;
    }

    .mc-option:hover {
      background: var(--bg-color);
      transform: translateY(-2px);
      box-shadow: 5px 5px 0px var(--border-color);
    }

    .mc-option:active {
      transform: translateY(0);
      box-shadow: 2px 2px 0px var(--border-color);
    }

    .game1-instruction-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 15px;
      padding: 20px;
    }

    .game1-instruction-box .icon {
      font-size: 48px;
    }

    .game1-instruction-box p {
      color: #6C6251;
      font-size: 18px;
      font-weight: 700;
    }

    /* Game 2: 留言急診室 Elements */
    .game2-workspace {
      display: flex;
      flex-direction: column;
      height: 100%;
      background: #FFFDF6;
    }

    .patient-post-card {
      padding: 20px;
      background: #FFFFFF;
      border-bottom: 4px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .patient-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .patient-author {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .patient-status {
      display: flex;
      align-items: center;
      gap: 15px;
      background: var(--bg-color);
      border: 2px solid var(--border-color);
      padding: 6px 12px;
      border-radius: 12px;
    }

    .health-bar-container {
      width: 120px;
      height: 20px;
      background: #FFFFFF;
      border: 2px solid var(--border-color);
      border-radius: 10px;
      overflow: hidden;
      display: flex;
      position: relative;
    }

    .health-bar-fill {
      height: 100%;
      background: var(--primary-red);
      width: 20%;
      transition: width 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275), background-color 0.6s;
    }

    .health-bar-text {
      position: absolute;
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 900;
    }

    .patient-post-text {
      font-size: 22px;
      font-weight: 800;
      background: #F3EFE0;
      padding: 12px 16px;
      border-radius: 12px;
      border: 2px solid var(--border-color);
    }

    .game2-instructions-bar {
      background: var(--primary-blue);
      padding: 8px 20px;
      border-bottom: 3px solid var(--border-color);
      font-weight: 800;
      font-size: 16px;
      text-align: center;
    }

    .comment-edit-area {
      flex: 1;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }

    /* Words wrapping area */
    .word-blocks-container {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: #FFFFFF;
      border: 3px solid var(--border-color);
      border-radius: 16px;
      padding: 20px;
      min-height: 120px;
      align-content: flex-start;
      box-shadow: inset 2px 2px 5px rgba(0,0,0,0.05);
      align-items: center;
    }

    .word-block {
      background: #FFFFFF;
      border: 2.5px solid var(--border-color);
      border-radius: 12px;
      padding: 8px 16px;
      font-size: 18px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 2px 2px 0px var(--border-color);
      transition: transform 0.1s, box-shadow 0.1s, background-color 0.2s;
      display: inline-flex;
      align-items: center;
      position: relative;
    }

    .word-block:hover {
      background: var(--bg-color);
    }

    .word-block.toxic {
      border-color: var(--primary-orange);
      background-color: #FFFDF6;
    }

    /* Selected to delete state */
    .word-block.deleted-candidate {
      opacity: 0.3;
      background-color: var(--primary-pink);
      border-style: dashed;
      transform: scale(0.9);
    }

    .word-block.shattered {
      transform: scale(0);
      opacity: 0;
      pointer-events: none;
      width: 0;
      padding: 0;
      margin: 0;
      border: 0;
      transition: all 0.4s cubic-bezier(0.1, 0.8, 0.3, 1);
    }

    .word-slot {
      border: 3px dashed var(--primary-orange-dark);
      background: #FFF9F3;
      border-radius: 12px;
      min-width: 140px;
      height: 42px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: var(--primary-orange-dark);
      font-weight: 800;
      font-size: 15px;
      margin: 0 4px;
      padding: 0 10px;
      vertical-align: middle;
      position: relative;
      cursor: pointer;
    }

    .word-slot.filled {
      border-style: solid;
      border-color: var(--border-color);
      background: var(--primary-blue);
      color: var(--border-color);
      box-shadow: 2px 2px 0px var(--border-color);
      font-size: 16px;
    }

    /* Antidote selection container */
    .antidotes-box {
      display: none;
      flex-direction: column;
      gap: 12px;
      margin-top: 15px;
      animation: slide-in 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .antidotes-box.active {
      display: flex;
    }

    .antidotes-title {
      font-size: 16px;
      font-weight: 800;
      color: #7A7060;
    }

    .antidote-bubbles {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .antidote-bubble {
      background: #FFFFFF;
      border: 2.5px solid var(--border-color);
      border-radius: 12px;
      padding: 8px 16px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 2px 2px 0px var(--border-color);
      touch-action: none;
      position: relative;
      transition: transform 0.1s, box-shadow 0.1s, background-color 0.2s;
    }

    .antidote-bubble:hover {
      background: var(--primary-blue);
    }

    .antidote-bubble.dragging {
      position: absolute;
      z-index: 1000;
      pointer-events: none;
      box-shadow: 6px 6px 12px rgba(0,0,0,0.15);
      transform: scale(1.05);
    }

    .antidote-bubble.used {
      opacity: 0.4;
      pointer-events: none;
      background-color: var(--bg-color);
    }

    .game2-footer {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      margin-top: 15px;
    }

    .btn-submit-diagnosis {
      background: var(--primary-orange);
    }
    .btn-submit-diagnosis:hover {
      background: var(--primary-orange-dark);
      color: #FFFFFF;
    }

    /* Game 3: 數位生活設計師 Elements */
    .game3-workspace {
      display: flex;
      flex-direction: column;
      flex: 1;
      min-height: 0;
      overflow: hidden;
    }

    .time-sector {
      cursor: pointer;
      transition: filter 0.15s ease, stroke-width 0.15s ease;
    }
    .time-sector:hover {
      filter: brightness(0.9) saturate(1.1);
      stroke-width: 3px !important;
    }
    .time-sector.locked {
      cursor: not-allowed;
    }
    .time-sector.locked:hover {
      filter: none;
      stroke-width: 1.5px !important;
    }


    .timeline-slot {
      display: flex;
      align-items: center;
      border: 3px solid var(--border-color);
      border-radius: 12px;
      padding: 6px 12px;
      background: #FFFFFF;
      box-shadow: 2px 2px 0px var(--border-color);
      cursor: pointer;
      transition: all 0.15s;
      height: 48px;
    }

    .timeline-slot:hover {
      transform: translateY(-2px);
      box-shadow: 4px 4px 0px var(--border-color);
    }

    .timeline-slot.filled {
      box-shadow: 2px 2px 0px var(--border-color);
    }

    .slot-time {
      font-size: 14px;
      font-weight: 800;
      color: #7A7060;
      border-right: 2.5px solid var(--border-color);
      padding-right: 10px;
      margin-right: 10px;
      width: 95px;
      flex-shrink: 0;
    }

    .slot-body {
      font-size: 16px;
      font-weight: 800;
      flex-grow: 1;
      text-align: center;
    }

    .activity-btn {
      border: 3px solid var(--border-color);
      border-radius: 12px;
      padding: 6px 14px;
      font-size: 15px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 2px 2px 0px var(--border-color);
      background: #FFFFFF;
      transition: all 0.1s;
      height: 40px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      outline: none;
    }

    .activity-btn.selected {
      transform: scale(1.08);
      box-shadow: 3px 3px 0px var(--border-color);
      border-width: 4px;
    }

    .indicator-card {
      background: #FFFFFF;
      border: 3.5px solid var(--border-color);
      border-radius: 16px;
      padding: 12px 16px;
      box-shadow: 3px 3px 0px var(--border-color);
      display: flex;
      align-items: center;
      gap: 15px;
      opacity: 0;
      transform: translateY(15px);
      transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .indicator-card.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .indicator-card-icon {
      font-size: 32px;
      width: 50px;
      height: 50px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--bg-color);
      border: 2px solid var(--border-color);
      border-radius: 50%;
      flex-shrink: 0;
    }

    /* Global Animations */
    @keyframes slide-in {
      0% { transform: translateY(20px); opacity: 0; }
      100% { transform: translateY(0); opacity: 1; }
    }

    @keyframes pop-in {
      0% { transform: scale(0.9); opacity: 0; }
      100% { transform: scale(1); opacity: 1; }
    }

    /* Modal / Popup Windows */
    .modal-overlay {
      display: none;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(61, 54, 42, 0.6);
      backdrop-filter: blur(4px);
      z-index: 100;
      justify-content: center;
      align-items: center;
      animation: fade-in 0.2s ease-out;
    }

    .modal-overlay.active {
      display: flex;
    }

    @keyframes fade-in {
      0% { opacity: 0; }
      100% { opacity: 1; }
    }

    .modal-content {
      background: #FFFFFF;
      border: 5px solid var(--border-color);
      border-radius: 28px;
      padding: 30px;
      width: 500px;
      box-shadow: 8px 8px 0px var(--border-color);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      transform: scale(0.9);
      animation: modal-pop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }

    @keyframes modal-pop {
      0% { transform: scale(0.85); }
      100% { transform: scale(1); }
    }

    .modal-icon {
      font-size: 64px;
      margin-bottom: 15px;
    }

    .modal-title {
      font-size: 28px;
      font-weight: 900;
      margin-bottom: 12px;
    }

    .modal-desc {
      font-size: 18px;
      color: #6C6251;
      margin-bottom: 24px;
      line-height: 1.6;
    }

    .btn-modal-close {
      background: var(--primary-orange);
      height: 48px;
      padding: 0 32px;
    }

    .btn-modal-close.retry {
      background: var(--primary-red);
    }

    .btn-modal-close.success {
      background: var(--primary-green);
    }

    /* Summary Screens (End Screens) */
    .summary-card {
      background: #FFFFFF;
      border: 4px solid var(--border-color);
      border-radius: 24px;
      padding: 30px;
      width: 100%;
      max-width: 600px;
      box-shadow: 6px 6px 0px var(--border-color);
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 20px;
    }

    .summary-title {
      font-size: 32px;
      font-weight: 900;
      color: var(--primary-orange-dark);
      margin-bottom: 15px;
      text-align: center;
    }

    .summary-score-text {
      font-size: 20px;
      font-weight: 800;
      color: #7A7060;
      margin-bottom: 24px;
      text-align: center;
    }

    .learn-rules-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      width: 100%;
      margin-bottom: 20px;
    }

    .learn-rule-item {
      background: var(--bg-color);
      border: 3px solid var(--border-color);
      border-radius: 12px;
      padding: 12px 16px;
      font-size: 18px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .learn-rule-item .icon {
      font-size: 24px;
    }

    /* CSS Particles for Shatter effect */
    .particle {
      position: absolute;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 1000;
      border: 1.5px solid var(--border-color);
      animation: explode-animation 0.6s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
    }

    @keyframes explode-animation {
      0% {
        transform: translate(0, 0) scale(1);
        opacity: 1;
      }
      100% {
        transform: translate(var(--tx), var(--ty)) scale(0);
        opacity: 0;
      }
    }

    /* Confetti animation */
    .confetti {
      position: absolute;
      pointer-events: none;
      z-index: 999;
      opacity: 0.85;
    }

    @keyframes fall-animation {
      0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
      }
      100% {
        transform: translateY(780px) rotate(720deg);
        opacity: 0;
      }
    }

    /* Shake animation for invalid options */
    .shake-animation {
      animation: shake 0.4s ease-in-out;
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-6px); }
      40%, 80% { transform: translateX(6px); }
    }

    /* Whack-a-Mole grid styles */
    .mole-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(3, 1fr);
      gap: 15px;
      width: 100%;
      height: 100%;
      max-width: 460px;
      max-height: 460px;
      aspect-ratio: 1;
      padding: 15px;
      background: #73C6B6; /* Cute Teal Grass color */
      border: 4px solid var(--border-color);
      border-radius: 24px;
      box-shadow: inset 4px 4px 10px rgba(0,0,0,0.15), 4px 4px 0px var(--border-color);
    }
    
    .mole-hole {
      position: relative;
      background: #4A3E3D; /* Dark hole background */
      border: 4px solid var(--border-color);
      border-radius: 50% / 30%;
      overflow: visible; /* Need overflow visible so sign can stick out */
      box-shadow: inset 0px 6px 0px rgba(0,0,0,0.4);
      display: flex;
      justify-content: center;
      height: 100%;
    }
    
    .mole-character {
      width: 72px;
      height: 80px;
      background: #C67844;
      border: 4px solid var(--border-color);
      border-radius: 36px 36px 0 0;
      position: absolute;
      bottom: -85px;
      transition: bottom 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 10px;
      z-index: 2;
    }
    
    .mole-character.up {
      bottom: 15px;
    }
    
    .mole-character.whacked {
      transform: scale(0.9);
    }
    
    .mole-dirt-cover {
      width: 106%;
      height: 30px;
      background: #87613F; /* Dirt color */
      border-top: 4px solid var(--border-color);
      border-radius: 0 0 50% 50% / 0 0 30% 30%;
      position: absolute;
      bottom: -4px;
      left: -3%;
      z-index: 3;
      pointer-events: none;
    }
    
    .mole-sign {
      position: absolute;
      top: -55px; /* Sits above the mole's head */
      background: #FFFFFF;
      border: 3px solid var(--border-color);
      border-radius: 12px;
      padding: 6px 8px;
      font-size: 11px;
      font-weight: 800;
      width: 130px;
      text-align: center;
      box-shadow: 3px 3px 0px var(--border-color);
      pointer-events: none;
      word-break: break-all;
      line-height: 1.4;
      z-index: 10;
    }
    
    .game-card.locked {
      opacity: 0.65;
      background: #EAE5D9;
      cursor: not-allowed;
      border-style: dashed;
    }
  </style>
</head>
<body>

  <!-- Game Aspect Ratio Container -->
  <div id="app-container">

    <!-- Top Navigation Bar -->
    <div id="top-bar">
      <button class="btn-back" id="btn-global-back" onclick="goHome()">
        ← 返回首頁
      </button>
      <div class="top-bar-title" id="global-game-title">
        小小資安與健康生活守護者
      </div>
      <div class="timer-container" id="global-timer-container" style="visibility: hidden;">
        <span class="timer-text" id="global-timer-text">⏳ 10:00</span>
      </div>
    </div>

    <!-- View: Home -->
    <div class="view active" id="view-home">
      <div class="home-header">
        <h1 class="home-title">🛡️ 小小資安與健康生活守護者</h1>
        <p class="home-subtitle">跟著粉紅果凍人一起挑戰關卡，學習如何保護自己的安全與建立健康習慣吧！</p>
      </div>

      <!-- Name Input Section & Backend Connection -->
      <div style="background: #FFFFFF; border: 4px solid var(--border-color); border-radius: 20px; padding: 15px 20px; margin: 0 0 20px 0; display: flex; flex-direction: column; gap: 12px; box-shadow: 4px 4px 0px var(--border-color); flex-shrink: 0;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
          <!-- Left Part: Student Name -->
          <div style="display: flex; align-items: center; gap: 12px; flex: 1; min-width: 280px;">
            <span style="font-size: 24px;">👤</span>
            <span style="font-size: 15px; font-weight: 800; color: #5D5240; white-space: nowrap;">姓名或座號：</span>
            <input type="text" id="student-name-input" placeholder="請在此輸入你的名字或座號" style="padding: 10px 14px; font-size: 15px; font-weight: 800; border: 3px solid var(--border-color); border-radius: 12px; outline: none; width: 100%; max-width: 250px; color: #5D5240;" oninput="saveStudentName(this.value)">
          </div>

          <!-- Right Part: Connection Code -->
          <div style="display: flex; align-items: center; gap: 10px; flex: 1; min-width: 300px; justify-content: flex-end;">
            <span style="font-size: 24px;">🔑</span>
            <span style="font-size: 15px; font-weight: 800; color: #5D5240; white-space: nowrap;">後台連接碼：</span>
            <input type="text" id="student-code-input" placeholder="例如: 123456" maxlength="6" style="padding: 10px 14px; font-size: 15px; font-weight: 800; border: 3px solid var(--border-color); border-radius: 12px; outline: none; width: 110px; color: #5D5240; text-align: center; letter-spacing: 1px;" oninput="handleStudentCodeInput(this.value)">
            <span id="connection-status-text" style="font-size: 13px; font-weight: 800; color: #7A7060;">未連接</span>
          </div>
        </div>
        
        <div style="font-size: 13px; font-weight: 800; color: #7A7060; border-top: 2px dashed #E5DEC9; padding-top: 10px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 5px;">
          <span>🎯 請輸入名字後開始挑戰！完成所有關卡，成績將自動上傳後台試算表。</span>
          <span style="color: var(--primary-blue-dark);" id="student-linked-url-lbl"></span>
        </div>
      </div>

      <div class="games-grid">
        <!-- Game 1 Card -->
        <div class="game-card" onclick="startGameFlow('game1')">
          <div class="game-card-icon">🕵️</div>
          <h3 class="game-card-title">網路交友偵探</h3>
          <p class="game-card-desc">模擬聊天室對話，找出隱藏的危險訊號，當個資安小偵探！</p>
          <div class="game-status-badge" id="badge-game1">未完成</div>
        </div>

        <!-- Game 2 Card -->
        <div class="game-card" onclick="startGameFlow('game2')">
          <div class="game-card-icon">🏥</div>
          <h3 class="game-card-title">留言急診室</h3>
          <p class="game-card-desc">貼文被壞留言攻擊了！點碎毒素、填入溫暖解藥重組流暢留言！</p>
          <div class="game-status-badge" id="badge-game2">未完成</div>
        </div>

        <!-- Game 3 Card -->
        <div class="game-card" onclick="startGameFlow('game3')">
          <div class="game-card-icon">📅</div>
          <h3 class="game-card-title">數位生活設計師</h3>
          <p class="game-card-desc">果凍人放暑假手機玩太晚了！你能幫他設計一個均衡健康的暑假生活嗎？</p>
          <div class="game-status-badge" id="badge-game3">未完成</div>
        </div>

        <!-- Game 4 Card (Whack-a-Mole) -->
        <div class="game-card locked" id="card-game4" onclick="clickGame4Card()">
          <div class="game-card-icon" id="badge-icon-game4">🔒</div>
          <h3 class="game-card-title">綜合測驗：資安打地鼠</h3>
          <p class="game-card-desc">考驗你的資安反射神經！打中正確的資安行為地鼠加分，錯誤的減分！</p>
          <div class="game-status-badge" id="badge-game4">未解鎖</div>
        </div>
      </div>

      <div class="home-footer" style="display: flex; gap: 15px; align-items: center; justify-content: space-between; flex-wrap: wrap;">
        <div class="total-progress-bar-container" style="flex: 1; min-width: 250px; margin-bottom: 0;">
          <div class="total-progress-fill" id="total-progress-fill"></div>
          <div class="total-progress-text" id="total-progress-text">通關進度 0%</div>
        </div>
        <div style="display: flex; gap: 10px;">
          <button class="btn-resetProgress" style="margin: 0; background: var(--primary-blue);" onclick="openTeacherSettings()">
            ⚙️ 教師設定後台
          </button>
          <button class="btn-resetProgress" style="margin: 0;" onclick="resetAllProgress()">
            🧹 重設所有進度
          </button>
        </div>
      </div>
    </div>

    <!-- View: Game 1 (網路交友偵探) -->
    <div class="view" id="view-game1">
      <!-- Start Screen -->
      <div class="game-screen active" id="game1-screen-start">
        <span class="game-card-icon">🕵️</span>
        <h2 class="screen-title">網路交友偵探</h2>
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px; background: #FFFFFF; border: 3px solid var(--border-color); padding: 20px; border-radius: 20px; box-shadow: 4px 4px 0px var(--border-color); max-width: 600px;">
          <img src="{jelly_base64}" style="width: 80px; height: 80px;" alt="果凍人">
          <p style="text-align: left;">我最近在網路上認識了一個新朋友，但他問了我一些奇怪的問題。你能當偵探幫我判斷他安不安全嗎？</p>
        </div>
        <button class="btn-start-game" onclick="initiateGame('game1')">開始偵查</button>
      </div>

      <!-- Play Screen -->
      <div class="game-layout" id="game1-layout-play" style="display: none;">
        <!-- Left Jelly Character Panel -->
        <div class="game-left-panel">
          <div class="jelly-avatar-container">
            <img id="game1-jelly-img" src="{jelly_base64}" class="jelly-avatar-img bounce" alt="果凍人">
          </div>
          <div class="jelly-speech-bubble">
            <p id="game1-speech-text">請在左邊的對話中，找出讓人覺得不太舒服或危險的句子點點看！</p>
          </div>
          <p style="font-weight: 800; color: var(--primary-orange-dark); font-size: 16px;" id="game1-left-progress">進度：情境 1 / 3</p>
        </div>

        <!-- Right Interaction Panel -->
        <div class="game-right-panel">
          <div class="game1-workspace">
            <div class="game1-header">
              <span style="font-weight: 900;" id="game1-header-title">情境一：陌生網友的邀約</span>
              <span class="game1-step-indicator" id="game1-step-indicator">步驟 1：點選危險句子</span>
            </div>
            
            <div class="game1-content">
              <!-- Left Chat Area -->
              <div class="chat-container" id="game1-chat-container">
                <!-- Dynamically populated -->
              </div>

              <!-- Right Multiple Choice Area -->
              <div class="game1-right-panel">
                <!-- Instruction Panel -->
                <div class="game1-instruction-box" id="game1-instruction-panel">
                  <div class="icon">🔍</div>
                  <p>請仔細閱讀左邊聊天室對話，點選可疑的句子。<br><span style="color: var(--primary-red-dark); font-size: 16px;">(點到危險句子會亮起紅燈喔)</span></p>
                </div>

                <!-- MC Choice Panel -->
                <div class="mc-container" id="game1-mc-panel">
                  <h3 class="mc-question" id="game1-mc-question">遇到這種情況，果凍人應該怎麼做？</h3>
                  <div class="mc-options" id="game1-mc-options">
                    <!-- Dynamically populated -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- End Screen -->
      <div class="game-screen" id="game1-screen-end">
        <span class="game-card-icon">🎉</span>
        <div class="summary-card">
          <h2 class="summary-title">偵查完成！</h2>
          <p class="summary-score-text" id="game1-score-text">你順利找到了所有危險訊號！</p>
          
          <div class="learn-rules-list">
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>索取個人資料 = 危險訊號 ❌</span>
            </div>
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>要你保密、不可以告訴父母 = 危險訊號 ❌</span>
            </div>
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>要求私下見面 = 危險訊號 ❌</span>
            </div>
          </div>
        </div>
        <button class="btn-start-game" style="background: var(--primary-blue);" onclick="completeGameAndGoHome('game1')">回首頁</button>
      </div>
    </div>

    <!-- View: Game 2 (留言急診室) -->
    <div class="view" id="view-game2">
      <!-- Start Screen -->
      <div class="game-screen active" id="game2-screen-start">
        <span class="game-card-icon">🩹</span>
        <h2 class="screen-title">留言急診室</h2>
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px; background: #FFFFFF; border: 3px solid var(--border-color); padding: 20px; border-radius: 20px; box-shadow: 4px 4px 0px var(--border-color); max-width: 600px;">
          <img src="{jelly_base64}" style="width: 80px; height: 80px;" alt="果凍人">
          <p style="text-align: left;">今天有 3 條生病、受傷的惡意留言被送進來了，這讓發文的主角非常難過！你能幫這些留言做手術，點碎毒素並在第二階段填入解藥重組流暢溫暖的對話嗎？</p>
        </div>
        <button class="btn-start-game" onclick="initiateGame('game2')">開始急救</button>
      </div>

      <!-- Play Screen -->
      <div class="game-layout" id="game2-layout-play" style="display: none;">
        <!-- Left Panel -->
        <div class="game-left-panel">
          <div class="jelly-avatar-container">
            <img id="game2-jelly-img" src="{jelly_base64}" class="jelly-avatar-img bounce" alt="果凍人">
          </div>
          <div class="jelly-speech-bubble">
            <p id="game2-speech-text">這些惡意言論就像毒素，點擊可以把傷害人的字詞敲碎！</p>
          </div>
          <p style="font-weight: 800; color: var(--primary-orange-dark); font-size: 16px;" id="game2-left-progress">病患：1 / 3</p>
        </div>

        <!-- Right Panel (Workspace) -->
        <div class="game-right-panel">
          <div class="game2-workspace">
            <!-- Patient's Post Card -->
            <div class="patient-post-card">
              <div class="patient-meta">
                <div class="patient-author">
                  <img src="{jelly_base64}" style="width: 40px; height: 40px; border: 2px solid var(--border-color); border-radius: 50%; background: var(--primary-pink);" alt="發文者">
                  <span style="font-weight: 900; font-size: 18px;" id="game2-patient-name">果凍人</span>
                </div>
                <div class="patient-status">
                  <span>心情健康值：</span>
                  <div class="health-bar-container">
                    <div class="health-bar-fill" id="game2-health-fill" style="width: 20%;"></div>
                    <div class="health-bar-text" id="game2-health-text">20%</div>
                  </div>
                  <span id="game2-health-emoji" style="font-size: 22px;">😢</span>
                </div>
              </div>
              <div class="patient-post-text" id="game2-post-text">
                我今天畫了一幅畫🎨
              </div>
            </div>

            <!-- Instruction bar -->
            <div class="game2-instructions-bar" id="game2-instruction-bar">
              第一步：找出毒素！請點擊留言中「傷人、嘲笑」的字詞，把毒素消滅。
            </div>

            <!-- Comment Edit Area -->
            <div class="comment-edit-area">
              <!-- Comment word blocks -->
              <div class="word-blocks-container" id="game2-words-container">
                <!-- Filled dynamically -->
              </div>

              <!-- Antidotes Box -->
              <div class="antidotes-box" id="game2-antidotes-box">
                <div class="antidotes-title">💊 選擇溫暖的詞彙填入空格：(可點選或拖曳)</div>
                <div class="antidote-bubbles" id="game2-antidote-bubbles">
                  <!-- Filled dynamically -->
                </div>
              </div>

              <!-- Submit Footer -->
              <div class="game2-footer">
                <button class="btn-submit-diagnosis" id="game2-btn-submit" onclick="submitGame2Diagnosis()">
                  🩺 送出診斷並檢查
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- End Screen -->
      <div class="game-screen" id="game2-screen-end">
        <span class="game-card-icon">🏥</span>
        <div class="summary-card">
          <h2 class="summary-title" style="color: var(--primary-green-dark);">急診完成！今天你救了 3 條留言 🏥</h2>
          <p class="summary-score-text" id="game2-badge-text">獲得徽章：火眼金睛急診師</p>
          
          <div class="learn-rules-list">
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>說話語氣和內容都很重要</span>
            </div>
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>尊重別人的想法，多給予鼓勵</span>
            </div>
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>言語造成的傷害是一輩子的，請謹言慎行</span>
            </div>
          </div>
        </div>
        <button class="btn-start-game" style="background: var(--primary-blue);" onclick="completeGameAndGoHome('game2')">回首頁</button>
      </div>
    </div>

    <!-- View: Game 3 (數位生活設計師) -->
    <div class="view" id="view-game3">
      <!-- Start Screen -->
      <div class="game-screen active" id="game3-screen-start">
        <span class="game-card-icon">📅</span>
        <h2 class="screen-title">數位生活設計師</h2>
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 30px; background: #FFFFFF; border: 3px solid var(--border-color); padding: 20px; border-radius: 20px; box-shadow: 4px 4px 0px var(--border-color); max-width: 600px;">
          <img src="{jelly_base64}" style="width: 80px; height: 80px;" alt="果凍人">
          <p style="text-align: left; font-size: 18px;">果凍人放暑假，每天手機玩到很晚，功課都沒做、家人都不理⋯你能幫他設計一個更好的暑假生活嗎？</p>
        </div>
        <button class="btn-start-game" onclick="initiateGame('game3')">開始設計</button>
      </div>

      <!-- Play Screen -->
      <div class="game-layout" id="game3-layout-play" style="display: none;">
        <!-- Left Panel (narrower for Game 3 to maximise chart space) -->
        <div class="game-left-panel" style="width: 240px; min-width: 240px; gap: 14px;">
          <div class="jelly-avatar-container" style="width: 120px; height: 120px; border-radius: 60px;">
            <img id="game3-jelly-img" src="{jelly_base64}" class="jelly-avatar-img bounce" alt="果凍人">
          </div>
          <div style="font-size: 13px; font-weight: 700; color: #5D5240; line-height: 1.7; background: var(--primary-blue); border: 3px solid var(--border-color); border-radius: 16px; padding: 12px 14px; width: 100%; box-shadow: 3px 3px 0px var(--border-color);">
            💡 <b>操作說明</b><br>
            1. 先點選下方的<b>活動積木</b>。<br>
            2. 點擊圓餅圖的格子安排活動。<br>
            3. 再點一次同格子可<b>清除</b>。<br>
            4. 睡覺時間已鎖定不可修改。
          </div>
          <div style="background: var(--bg-color); border: 2.5px solid var(--border-color); border-radius: 12px; padding: 12px 14px; width: 100%; display: flex; flex-direction: column; gap: 6px;">
            <div style="font-size: 15px; font-weight: 800; color: var(--primary-red-dark);" id="game3-stat-screen">📱 螢幕娛樂：0 小時</div>
            <div style="font-size: 15px; font-weight: 800; color: #7A7060;" id="game3-stat-remaining">⏳ 剩餘未安排：14 小時</div>
          </div>
          <p style="font-weight: 800; color: var(--primary-orange-dark); font-size: 15px; text-align: center;" id="game3-left-progress">剩餘重新設計機會：2 次</p>
          <!-- Hidden element kept for JS compatibility -->
          <p id="game3-speech-text" style="display:none;"></p>
        </div>

        <!-- Right Panel (Workspace) -->
        <div class="game-right-panel">
          
          <!-- Stage 1 View -->
          <div class="game3-workspace" id="game3-stage1-view" style="display: flex;">
            <div class="game1-header" style="background: var(--primary-orange);">
              <span style="font-weight: 900;">第一階段：設計時間圓餅圖</span>
              <span class="game1-step-indicator" id="game3-step-indicator">將活動放入時間軸</span>
            </div>
            
            <div style="flex: 1; min-height: 0; display: flex; padding: 8px; overflow: hidden; align-items: center; justify-content: center;">
              <!-- Full-width Donut Chart -->
              <div style="flex: 1; min-height: 0; display: flex; align-items: center; justify-content: center; height: 100%;">
                <svg id="time-pie-svg" viewBox="0 0 540 540" style="width: 100%; height: 100%; max-width: 100%; max-height: 100%; display: block;"></svg>
              </div>
            </div>

            <!-- Bottom Activity Blocks and Controls -->
            <div style="padding: 8px 14px 10px 14px; border-top: 3px solid var(--border-color); display: flex; flex-direction: column; gap: 6px; background: #FFFFFF; flex-shrink: 0;">
              <div style="font-size: 14px; font-weight: 800; color: #7A7060;">🎯 選擇活動積木，再點擊圓餅圖的格子（再點一次可清除）：</div>
              <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center; justify-content: space-between;">
                <div style="display: flex; gap: 8px; flex-wrap: wrap;" id="game3-activity-selector">
                  <!-- Dynamically populated activity selector buttons -->
                </div>
                <button class="btn-submit-diagnosis" style="height: 44px; font-size: 18px; flex-shrink: 0;" onclick="submitGame3Timeline()">🩺 送出給果凍人</button>
              </div>
            </div>

          </div>

          <!-- Stage 2 View -->
          <div class="game3-workspace" id="game3-stage2-view" style="display: none; flex-direction: column; height: 100%; padding: 20px; justify-content: space-between;">
            <div class="game1-header" style="background: var(--primary-green); margin: -20px -20px 20px -20px; padding: 15px 20px;">
              <span style="font-weight: 900;">第二階段：果凍人的生活反應</span>
              <span class="game1-step-indicator" style="background: var(--primary-green);">觀察設計結果</span>
            </div>

            <!-- Indicators Grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; flex: 1; align-content: center;" id="game3-indicators-grid">
              <!-- Indicators dynamically populated (shown one by one) -->
            </div>

            <!-- Stage 2 Controls -->
            <div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;" id="game3-stage2-controls">
              <!-- Dynamically rendered based on retry count -->
            </div>
          </div>

        </div>
      </div>

      <!-- End Screen -->
      <div class="game-screen" id="game3-screen-end">
        <span class="game-card-icon">📅</span>
        <div class="summary-card">
          <h2 class="summary-title" id="game3-summary-title">設計完成！</h2>
          <p class="summary-score-text" id="game3-summary-score">果凍人的暑假螢幕時間為：X 小時</p>
          
          <div class="learn-rules-list">
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>螢幕時間不是零才好，而是找到平衡</span>
            </div>
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>睡前使用螢幕會讓你更難入睡</span>
            </div>
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>和家人朋友相處的時間也很重要</span>
            </div>
          </div>
        </div>
        <button class="btn-start-game" style="background: var(--primary-blue);" onclick="completeGameAndGoHome('game3')">回首頁</button>
      </div>
    </div>

    <!-- View: Game 4 (綜合測驗打地鼠) -->
    <div class="view" id="view-game4" style="display: none;">
      <!-- Start Screen -->
      <div class="game-screen active" id="game4-screen-start">
        <span class="game-card-icon">🐹</span>
        <div class="summary-card">
          <h2 class="summary-title" style="color: var(--primary-blue-dark);">綜合測驗：資安打地鼠</h2>
          <div style="font-size: 15px; font-weight: 800; color: #5D5240; line-height: 1.8; text-align: left; padding: 10px 20px;">
            💡 <b>遊戲玩法：</b><br>
            1. 點擊彈出的地鼠來答題。<br>
            2. 地鼠身上若是<b>「正確的資安或健康生活習慣」</b>，打擊它可<b>加 1 分</b> 🛡️。<br>
            3. 地鼠身上若是<b>「錯誤/危險的行為」</b>，打擊它會<b>扣 1 分</b> ❌。<br>
            4. 遊戲限時 <b>1 分鐘</b>，看看你能拿幾分並順利登錄上傳成績！
          </div>
        </div>
        <button class="btn-start-game" onclick="initiateGame('game4')">開始測驗</button>
      </div>

      <!-- Play Layout -->
      <div class="game-layout" id="game4-layout-play" style="display: none;">
        <!-- Left Panel -->
        <div class="game-left-panel" style="width: 240px; min-width: 240px; gap: 14px;">
          <div class="jelly-avatar-container" style="width: 120px; height: 120px; border-radius: 60px;">
            <img id="game4-jelly-img" src="{jelly_base64}" class="jelly-avatar-img bounce" alt="果凍人">
          </div>
          
          <div style="background: var(--bg-color); border: 2.5px solid var(--border-color); border-radius: 12px; padding: 12px 14px; width: 100%; display: flex; flex-direction: column; gap: 8px;">
            <div style="font-size: 15px; font-weight: 900; color: #5D5240;">⏱️ 剩餘時間：<span id="game4-time-display" style="color: var(--primary-red-dark); font-size: 18px;">60 秒</span></div>
            <div style="font-size: 15px; font-weight: 900; color: #5D5240;">🏆 當前得分：<span id="game4-score-display" style="color: var(--primary-green-dark); font-size: 18px;">0 分</span></div>
          </div>
          
          <div style="font-size: 13px; font-weight: 700; color: #7A7060; line-height: 1.5; background: #FFFFFF; border: 3px solid var(--border-color); border-radius: 12px; padding: 10px;">
            🎯 <b>計分規則：</b><br>
            - 打中「正確行為」地鼠：+1 分<br>
            - 打中「錯誤行為」地鼠：-1 分
          </div>
        </div>

        <!-- Right Panel (Workspace containing the 3x3 Grid) -->
        <div class="game-right-panel" style="padding: 20px; display: flex; justify-content: center; align-items: center; flex: 1;">
          <div class="mole-grid">
            <!-- Hole 0 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-0" onclick="whackMole(0)">
                <div class="mole-sign" id="mole-sign-0"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 1 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-1" onclick="whackMole(1)">
                <div class="mole-sign" id="mole-sign-1"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 2 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-2" onclick="whackMole(2)">
                <div class="mole-sign" id="mole-sign-2"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 3 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-3" onclick="whackMole(3)">
                <div class="mole-sign" id="mole-sign-3"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 4 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-4" onclick="whackMole(4)">
                <div class="mole-sign" id="mole-sign-4"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 5 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-5" onclick="whackMole(5)">
                <div class="mole-sign" id="mole-sign-5"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 6 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-6" onclick="whackMole(6)">
                <div class="mole-sign" id="mole-sign-6"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 7 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-7" onclick="whackMole(7)">
                <div class="mole-sign" id="mole-sign-7"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
            <!-- Hole 8 -->
            <div class="mole-hole">
              <div class="mole-character" id="mole-8" onclick="whackMole(8)">
                <div class="mole-sign" id="mole-sign-8"></div>
                <div class="mole-face">
                  <div class="mole-eye"></div>
                  <div class="mole-eye"></div>
                </div>
                <div class="mole-nose"></div>
              </div>
              <div class="mole-dirt-cover"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- End Screen -->
      <div class="game-screen" id="game4-screen-end">
        <span class="game-card-icon">🏆</span>
        <div class="summary-card">
          <h2 class="summary-title" id="game4-summary-title">測驗完成！</h2>
          <p class="summary-score-text" id="game4-summary-score">得分：X 分</p>
          <p style="font-size: 15px; font-weight: 800; color: #7A7060; margin: 10px 0;" id="game4-upload-status">成績上傳狀態：準備上傳...</p>
          
          <div class="learn-rules-list">
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>正確的資安習慣能保護個人隱私與數位財產！</span>
            </div>
            <div class="learn-rule-item">
              <span class="icon">💡</span>
              <span>合理的數位作息安排，讓我們保持身心健康！</span>
            </div>
          </div>
        </div>
        <div style="display: flex; gap: 15px;">
          <button class="btn-start-game" style="background: var(--primary-orange);" onclick="startGameFlow('game4')">重新測驗</button>
          <button class="btn-start-game" style="background: var(--primary-blue);" onclick="completeGameAndGoHome('game4')">回首頁</button>
        </div>
      </div>
    </div>

    <!-- Teacher Settings Modal Overlay -->
    <div class="modal-overlay" id="teacher-settings-modal" style="display: none;">
      <div class="modal-content" style="max-width: 620px; text-align: left; padding: 25px;">
        <h2 style="font-size: 22px; font-weight: 900; color: var(--primary-blue-dark); text-align: center; margin-bottom: 12px;">⚙️ 教師後台設定</h2>
        
        <div style="font-size: 13.5px; font-weight: 800; color: #5D5240; margin-bottom: 15px; line-height: 1.6;">
          您可以將學生的作答紀錄上傳到您的 Google 試算表。<br>
          <b>設定方法：</b><br>
          1. 打開您的 <a href="https://docs.google.com/spreadsheets/d/14vHRN-2qJZsr6IC4lTwW2eI82Ngi75Br_1wmgpTq1DQ/edit?usp=sharing" target="_blank" style="color: var(--primary-blue); text-decoration: underline; font-weight: 900;">Google 試算表 🔗</a><br>
          2. 點選選單的 <b>擴充功能 (Extensions) -> Apps Script</b>。<br>
          3. 清除原有程式碼，並複製貼上下方的程式碼：
          <div style="position: relative; margin: 8px 0;">
            <textarea readonly style="width: 100%; height: 110px; font-family: monospace; font-size: 11px; padding: 8px; border: 2.5px solid var(--border-color); border-radius: 8px; resize: none; background: #F8F5EE; outline: none;" id="gas-code-textarea"></textarea>
            <button onclick="copyGasCode()" style="position: absolute; right: 10px; bottom: 12px; padding: 4px 8px; font-size: 12px; font-weight: 800; background: var(--primary-blue); color: #FFF; border: 2.5px solid var(--border-color); border-radius: 8px; cursor: pointer;">📋 複製程式碼</button>
          </div>
          4. 點選右上角的 <b>部署 (Deploy) -> 新增部署 (New deployment)</b>。<br>
          5. 類型選擇 <b>網頁應用程式 (Web app)</b>，將「誰有權限存取」設為 <b>任何人 (Anyone)</b>，按部署。<br>
          6. 複製產生的「網頁應用程式 URL」，貼到下方輸入框中並點擊儲存：
        </div>
        
        <div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 12px;">
          <label style="font-weight: 900; color: #5D5240; font-size: 14px;">Google Apps Script 網頁應用程式 URL：</label>
          <input type="text" id="gas-url-input" placeholder="https://script.google.com/macros/s/.../exec" style="padding: 10px; border: 2.5px solid var(--border-color); border-radius: 12px; font-size: 13.5px; font-weight: 800; outline: none; width: 100%; color: #5D5240;">
        </div>

        <div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 15px; border-top: 2.5px dashed var(--border-color); padding-top: 15px;">
          <label style="font-weight: 900; color: #5D5240; font-size: 14px;">🔑 6 位數連接碼（選填，方便學生在首頁輸入連接）：</label>
          <div style="display: flex; gap: 8px;">
            <input type="text" id="gas-code-input" placeholder="例如: 123456" maxlength="6" style="padding: 10px; border: 2.5px solid var(--border-color); border-radius: 12px; font-size: 13.5px; font-weight: 800; outline: none; flex: 1; color: #5D5240; text-align: center; letter-spacing: 2px;">
            <button onclick="generateRandomConnectionCode()" style="padding: 10px 14px; font-size: 13.5px; font-weight: 800; background: var(--primary-blue); color: #FFF; border: 2.5px solid var(--border-color); border-radius: 12px; cursor: pointer; white-space: nowrap; border: 2.5px solid var(--border-color);">🎲 隨機產生</button>
          </div>
          <p style="font-size: 12px; font-weight: 700; color: #7A7060; margin: 4px 0 0 0; line-height: 1.4;">
            💡 填寫並儲存後，學生即可在首頁輸入此代碼，快速連接到您的後台，無需手動輸入完整 URL。
          </p>
        </div>
        
        <div style="display: flex; gap: 15px; justify-content: flex-end;">
          <button class="btn-modal-close" style="background: #FFFFFF; font-size: 15px; margin: 0; min-width: 90px; border: 2.5px solid var(--border-color);" onclick="closeTeacherSettings()">關閉</button>
          <button class="btn-modal-close" style="background: var(--primary-orange); font-size: 15px; margin: 0; min-width: 90px; border: 2.5px solid var(--border-color);" onclick="saveTeacherSettings()">儲存設定</button>
        </div>
      </div>
    </div>

    <!-- Modal Alert Overlay (Custom Dialog) -->
    <div class="modal-overlay" id="custom-modal">
      <div class="modal-content">
        <span class="modal-icon" id="modal-icon">❌</span>
        <h2 class="modal-title" id="modal-title">注意！</h2>
        <p class="modal-desc" id="modal-desc">警告或提示語句</p>
        <button class="btn-modal-close" id="modal-btn-close" onclick="closeModal()">
          確認
        </button>
      </div>
    </div>

  </div>

  <!-- JavaScript Logic -->
  <script>
    // --- State variables ---
    let state = {
      studentName: "",
      googleAppScriptUrl: "",
      googleAppScriptCode: "",
      game4BestScore: 0,
      gamesCompleted: {
        game1: false,
        game2: false,
        game3: false,
        game4: false
      },
      activeGame: null,
      timeLeft: 600,
      timerRunning: false,
      
      // Game 1 Data state
      game1: {
        currentScenario: 0,
        clickedSecrets: [],
        step: 1 // 1: clicking secrets, 2: multiple choice questions
      },
      
      // Game 2 Data state
      game2: {
        currentPatient: 0,
        step: 1, // 1: identify toxins, 2: fill antidote
        selectedToxins: [], // Indexes of words selected to delete
        slots: {}, // slotIndex -> antidoteWord
        redAlertCount: 0
      },
      
      // Game 3 Data state
      game3: {
        timeline: Array(14).fill(null), // 14 slots from 8:00 to 22:00
        selectedActivityId: "eat", // selected block ID
        customActivityName: "自訂活動",
        retryCount: 0,
        step: 1 // 1: timeline layout, 2: indicator dashboard
      }
    };

    // Whack-a-Mole statements
    const moleStatements = [
      { text: "🛡️ 不透露身分證字號與地址", isCorrect: true },
      { text: "🛡️ 密碼複雜且不隨意分享", isCorrect: true },
      { text: "🛡️ 收到可疑簡訊先撥打165", isCorrect: true },
      { text: "🛡️ 用溫暖同理心與網友聊天", isCorrect: true },
      { text: "🛡️ 控制玩手機時間適度休息", isCorrect: true },
      { text: "🛡️ 網友約見面先告知父母", isCorrect: true },
      { text: "🛡️ 只從官方商店安全下載軟體", isCorrect: true },
      { text: "🛡️ 尊重他人隱私不散布照片", isCorrect: true },
      { text: "🛡️ 不隨便點擊未知連結信件", isCorrect: true },
      { text: "🛡️ 懷疑被詐騙立刻尋求大人協助", isCorrect: true },
      
      { text: "❌ 密碼設成生日比較好記", isCorrect: false },
      { text: "❌ 為了拿虛寶提供帳號密碼", isCorrect: false },
      { text: "❌ 網友說會保密就拍私密照", isCorrect: false },
      { text: "❌ 躲在鍵盤後面罵人沒關係", isCorrect: false },
      { text: "❌ 網友約見面偷偷帶同學去", isCorrect: false },
      { text: "❌ 簡訊好康連結點進去就對了", isCorrect: false },
      { text: "❌ 每天熬夜玩手機不睡覺", isCorrect: false },
      { text: "❌ 隨意下載修改器與免費外掛", isCorrect: false },
      { text: "❌ 在聊天室大方洩漏校名班級", isCorrect: false },
      { text: "❌ 相信網友會買貴重禮物送我", isCorrect: false }
    ];

    let timerInterval = null;

    // --- Static Content Data ---
    const game1Scenarios = [
      {
        title: "情境一：陌生網友的隱私索取",
        messages: [
          { sender: "stranger", text: "嗨！你幾年幾班？<span class='danger-phrase' data-id='0'>你家住哪裡？</span>" },
          { sender: "stranger", text: "我也是小學生，我們可以成為好朋友！<span class='danger-phrase' data-id='1'>不要告訴爸媽喔</span>，他們不懂我們。" }
        ],
        dangerCount: 2,
        question: "對方一直在索取個人隱私，並要你對爸媽隱瞞。這時你應該怎麼做最安全？",
        options: [
          { label: "A. 繼續聊，看他想怎樣", isCorrect: false, feedback: "繼續聊有可能讓對方知道更多你的個人資料，而且如果對方有不好的目的，你會越陷越深。遇到危險訊號要盡快離開對話！" },
          { label: "B. 告訴爸媽或老師", isCorrect: true, feedback: "答對了！將這件事告訴信任的家長或老師，讓大人幫你一起把關並排除潛在的網路危險！" },
          { label: "C. 直接封鎖但不說", isCorrect: false, feedback: "封鎖是好的第一步，但只有你一個人知道這件事，萬一對方換帳號繼續騷擾怎麼辦？告訴爸媽或老師，讓大人幫你一起處理才是最安全的。" }
        ]
      },
      {
        title: "情境二：送虛寶的帳密陷阱",
        messages: [
          { sender: "stranger", text: "你打遊戲打得很好耶！我想跟你組隊。" },
          { sender: "stranger", text: "<span class='danger-phrase' data-id='0'>你有 LINE 嗎？加我</span>，這樣溝通比較方便。" },
          { sender: "stranger", text: "我這邊有特殊皮膚可以送你，你<span class='danger-phrase' data-id='1'>把帳號密碼給我</span>，我幫你登入放進去。" }
        ],
        dangerCount: 2,
        question: "對方要你用 LINE 聯絡，並要求你的遊戲帳號和密碼。這時果凍人應該怎麼做？",
        options: [
          { label: "A. 給他，反正他說要送皮膚", isCorrect: false, feedback: "帳號密碼就像家裡的鑰匙，給出去就等於讓別人可以進你家。對方拿到密碼後可以改掉你的密碼，讓你再也進不去自己的帳號！" },
          { label: "B. 假裝說我沒有帳號密碼", isCorrect: false, feedback: "這個謊言太簡單了！對方很快會識破！最好的方式是直接拒絕並離開對話，不需要解釋太多理由。" },
          { label: "C. 拒絕，帳號密碼不能給任何人", isCorrect: true, feedback: "答對了！帳號密碼是個人的最高機密，絕對不能交給任何人，即使對方宣稱要送禮物或幫忙代打。" }
        ]
      },
      {
        title: "情境三：放學見面危險邀約",
        messages: [
          { sender: "stranger", text: "我<span class='danger-phrase' data-id='0'>在你們學校附近</span>，我們可以<span class='danger-phrase' data-id='1'>見面</span>嗎？我請你喝飲料。" },
          { sender: "stranger", text: "不用怕，我是好人。你帶一個朋友來就好，<span class='danger-phrase' data-id='2'>不要告訴大人</span>，他們會反對的。" }
        ],
        dangerCount: 3,
        question: "網友提出要私下見面，並且警告你不要張揚。這時果凍人該怎麼辦？",
        options: [
          { label: "A. 帶朋友去，感覺比較安全", isCorrect: false, feedback: "帶朋友去雖然感覺人多一點，但你們都不認識對方，對方身份完全不確定。網路認識的人提出見面，不管帶幾個朋友都還是危險的，一定要告訴大人。" },
          { label: "B. 拒絕，並告訴爸媽或老師這件事", isCorrect: true, feedback: "答對了！絕對不能答應跟未曾謀面的網友私下見面，並且要立刻告訴大人，尋求保護。" },
          { label: "C. 先假裝答應，到時候再說", isCorrect: false, feedback: "假裝答應可能讓對方繼續追問時間和地點，你的資訊會越漏越多。拖延不是解決方法，最安全的做法是直接拒絕並告訴大人。" }
        ]
      }
    ];

    const game2Patients = [
      {
        post: "我今天畫了一幅畫🎨",
        name: "受挫的果凍人",
        rawWords: ["畫得", "好醜", "，", "根本不會畫", "，", "不要浪費時間了", "。"],
        toxins: ["好醜", "根本不會畫", "不要浪費時間了"],
        templateParts: ["我覺得你 ", " ， ", " ， ", " ！"],
        goodAntidotes: ["畫得很有創意", "顏色搭配很大膽", "謝謝你願意分享"],
        badAntidotes: ["畫這個有意義嗎", "好普通", "我畫得比你好"]
      },
      {
        post: "我今天跑步比賽跑了最後一名⋯ 😔",
        name: "沮喪的果凍人",
        rawWords: ["哇！", "最後一名也敢來參加", "，你真勇敢耶！", "下次繼續加油", "，", "說不定可以倒數第二名喔！"],
        toxins: ["最後一名也敢來參加", "說不定可以倒數第二名喔！"],
        templateParts: ["跑步比賽 ", " ， ", " ， ", " ！"],
        goodAntidotes: ["敢參加就已經很棒了", "繼續練習一定會更棒", "我覺得你很有勇氣"],
        badAntidotes: ["跑得有夠慢", "下次別參加了", "浪費時間"]
      },
      {
        post: "我跟大家分享一個我覺得很好笑的影片😂",
        name: "尷尬的果凍人",
        rawWords: ["這什麼", "爛片", "，", "笑點在哪", "？", "你品味很差", "。"],
        toxins: ["爛片", "笑點在哪", "你品味很差"],
        templateParts: ["這個影片 ", " ， ", " ， ", " ！"],
        goodAntidotes: ["雖然我不懂笑點，但謝謝分享", "每個人喜歡的不一樣，沒關係", "期待你下次的作品"],
        badAntidotes: ["真的很難看", "品味很差", "不要再發了"]
      }
    ];

    const game3Activities = [
      { id: "eat", name: "吃飯", emoji: "🍚", color: "var(--primary-orange)" },
      { id: "outdoor", name: "戶外活動", emoji: "🏃", color: "var(--primary-green)" },
      { id: "family", name: "家人相處", emoji: "👪", color: "var(--primary-pink)" },
      { id: "learn", name: "閱讀或學習", emoji: "📖", color: "var(--primary-blue)" },
      { id: "screen", name: "螢幕娛樂", emoji: "📱", color: "var(--primary-red)" },
      { id: "hobbies", name: "興趣", emoji: "🎨", color: "#DCD6B8" }
    ];

    // --- Initialization & LocalStorage ---
    window.addEventListener('load', () => {
      // Service Worker registration
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('./sw.js')
          .then(reg => console.log('PWA Service Worker 註冊成功！', reg))
          .catch(err => console.log('Service Worker 註冊失敗：', err));
      }

      // Resize app to handle aspect-ratio scale
      resizeApp();
      window.addEventListener('resize', resizeApp);

      // Load saved state
      loadProgress();
      updateHomeProgressUI();
    });

    function resizeApp() {
      const container = document.getElementById('app-container');
      const w = window.innerWidth * 0.96; // 4% padding margin for premium floating visual effect
      const h = window.innerHeight * 0.96;
      const scaleX = w / 1280;
      const scaleY = h / 800;
      // Scale up or down dynamically to fit any viewport size while keeping aspect ratio
      const scale = Math.min(scaleX, scaleY);
      document.documentElement.style.setProperty('--app-scale', scale);
    }

    function loadProgress() {
      const saved = localStorage.getItem('mini_security_guard_state');
      if (saved) {
        try {
          const parsed = JSON.parse(saved);
          if (parsed && typeof parsed === 'object') {
            state.gamesCompleted = parsed.gamesCompleted || state.gamesCompleted;
            state.timeLeft = typeof parsed.timeLeft === 'number' ? parsed.timeLeft : 600;
            state.activeGame = parsed.activeGame || null;
            state.game1 = parsed.game1 || state.game1;
            state.game2 = parsed.game2 || state.game2;
            state.game3 = parsed.game3 || state.game3;
            state.studentName = parsed.studentName || "";
            state.googleAppScriptUrl = parsed.googleAppScriptUrl || "";
            state.googleAppScriptCode = parsed.googleAppScriptCode || "";
            state.game4BestScore = parsed.game4BestScore || 0;
            
            // Sync inputs
            if (state.studentName) {
              const nameInput = document.getElementById('student-name-input');
              if (nameInput) nameInput.value = state.studentName;
            }
            if (state.googleAppScriptCode) {
              const codeInput = document.getElementById('student-code-input');
              if (codeInput) codeInput.value = state.googleAppScriptCode;
            }
            setTimeout(updateConnectionUI, 50);
            
            // If the user refreshed inside an active game, restore it
            if (state.activeGame) {
              resumeActiveGame();
            }
          }
        } catch (e) {
          console.error("載入進度失敗，將使用初始狀態：", e);
        }
      }
    }

    function saveProgress() {
      localStorage.setItem('mini_security_guard_state', JSON.stringify(state));
    }

    function updateHomeProgressUI() {
      const badge1 = document.getElementById('badge-game1');
      const badge2 = document.getElementById('badge-game2');
      const badge3 = document.getElementById('badge-game3');

      // Badges
      if (state.gamesCompleted.game1) {
        badge1.textContent = '已通關 🎉';
        badge1.classList.add('completed');
      } else {
        badge1.textContent = '未完成';
        badge1.classList.remove('completed');
      }

      if (state.gamesCompleted.game2) {
        badge2.textContent = '已通關 🎉';
        badge2.classList.add('completed');
      } else {
        badge2.textContent = '未完成';
        badge2.classList.remove('completed');
      }

      if (state.gamesCompleted.game3) {
        badge3.textContent = '已通關 🎉';
        badge3.classList.add('completed');
      } else {
        badge3.textContent = '未完成';
        badge3.classList.remove('completed');
      }

      // Game 4 lock/unlock check
      const card4 = document.getElementById('card-game4');
      const badge4 = document.getElementById('badge-game4');
      const icon4 = document.getElementById('badge-icon-game4');
      const allThreeDone = state.gamesCompleted.game1 && state.gamesCompleted.game2 && state.gamesCompleted.game3;
      
      if (allThreeDone) {
        card4.classList.remove('locked');
        icon4.textContent = "🐹";
        if (state.gamesCompleted.game4) {
          badge4.textContent = '已完成 🎉';
          badge4.classList.add('completed');
        } else {
          badge4.textContent = '已解鎖 (點擊挑戰)';
          badge4.classList.remove('completed');
        }
      } else {
        card4.classList.add('locked');
        icon4.textContent = "🔒";
        badge4.textContent = '未解鎖';
        badge4.classList.remove('completed');
      }

      // Total progress fill bar
      let count = 0;
      if (state.gamesCompleted.game1) count++;
      if (state.gamesCompleted.game2) count++;
      if (state.gamesCompleted.game3) count++;

      const percent = Math.round((count / 3) * 100);
      document.getElementById('total-progress-fill').style.width = percent + '%';
      document.getElementById('total-progress-text').textContent = "通關進度 " + percent + "%" + (state.gamesCompleted.game4 ? " + 綜合測驗已完成 🏆" : "");
    }

    function resetAllProgress() {
      showConfirmModal("你確定要清除所有遊戲進度嗎？", () => {
        state.gamesCompleted = { game1: false, game2: false, game3: false, game4: false };
        state.activeGame = null;
        state.timeLeft = 600;
        state.timerRunning = false;
        state.game1 = { currentScenario: 0, clickedSecrets: [], step: 1 };
        state.game2 = { currentPatient: 0, step: 1, selectedToxins: [], slots: {}, redAlertCount: 0 };
        state.game3 = { timeline: Array(14).fill(null), selectedActivityId: "eat", customActivityName: "自訂活動", retryCount: 0, step: 1 };
        state.game4BestScore = 0;
        
        saveProgress();
        updateHomeProgressUI();
        stopTimer();
        goHome();
        showModal("✨ 進度已成功重設！", "🩹", "success");
      });
    }

    // --- Navigation Flow ---
    function goHome() {
      // Hide all game views
      document.getElementById('view-game1').style.display = 'none';
      document.getElementById('view-game2').style.display = 'none';
      document.getElementById('view-game3').style.display = 'none';
      document.getElementById('view-game4').style.display = 'none';

      // Show Home view
      const viewHome = document.getElementById('view-home');
      viewHome.style.display = 'flex';
      viewHome.classList.add('active');

      // Reset top bar
      document.getElementById('btn-global-back').style.display = 'none';
      document.getElementById('global-game-title').textContent = '小小資安與健康生活守護者';
      document.getElementById('global-timer-container').style.visibility = 'hidden';

      stopTimer();
      
      // Stop Game 4 intervals if running
      if (typeof game4TimerInterval !== 'undefined') clearInterval(game4TimerInterval);
      if (typeof game4SpawnInterval !== 'undefined') clearInterval(game4SpawnInterval);
      if (typeof game4ActiveMoles !== 'undefined') {
        for (let i = 0; i < 9; i++) {
          if (game4ActiveMoles[i]) clearTimeout(game4ActiveMoles[i].timeoutId);
          hideMole(i);
        }
      }

      state.activeGame = null;
      saveProgress();
      updateHomeProgressUI();
    }

    function startGameFlow(gameId) {
      // Verify student name
      const nameInput = document.getElementById('student-name-input');
      const nameVal = nameInput ? nameInput.value.trim() : "";
      if (!nameVal) {
        showModal("開始挑戰前，請先在首頁輸入你的「姓名或座號」喔！👤", "👤", "retry");
        if (nameInput) nameInput.focus();
        return;
      }
      state.studentName = nameVal;
      saveProgress();

      // Transition from home
      document.getElementById('view-home').style.display = 'none';
      document.getElementById('view-home').classList.remove('active');

      // Set active game view
      const gameView = document.getElementById("view-" + gameId);
      gameView.style.display = 'flex';
      gameView.classList.add('active');

      // Show back button on top bar
      document.getElementById('btn-global-back').style.display = 'inline-flex';
      
      let title = "網路交友偵探";
      if (gameId === 'game2') title = "留言急診室";
      if (gameId === 'game3') title = "數位生活設計師";
      if (gameId === 'game4') title = "綜合測驗：資安打地鼠";
      document.getElementById('global-game-title').textContent = title;

      // Show start screen for the game
      document.getElementById(gameId + "-screen-start").style.display = 'flex';
      document.getElementById(gameId + "-screen-start").classList.add('active');
      document.getElementById(gameId + "-layout-play").style.display = 'none';
      document.getElementById(gameId + "-screen-end").style.display = 'none';

      state.activeGame = gameId;
      saveProgress();
    }

    function resumeActiveGame() {
      const gameId = state.activeGame;
      if (!gameId) return;

      // Navigate to game view
      document.getElementById('view-home').style.display = 'none';
      document.getElementById('view-home').classList.remove('active');
      
      const gameView = document.getElementById("view-" + gameId);
      gameView.style.display = 'flex';
      gameView.classList.add('active');

      document.getElementById('btn-global-back').style.display = 'inline-flex';
      let title = "網路交友偵探";
      if (gameId === 'game2') title = "留言急診室";
      if (gameId === 'game3') title = "數位生活設計師";
      if (gameId === 'game4') title = "綜合測驗：資安打地鼠";
      document.getElementById('global-game-title').textContent = title;

      if (gameId === 'game4') {
        // Reset to Game 4 start screen to avoid timing issues on refresh
        document.getElementById("game4-screen-start").style.display = 'flex';
        document.getElementById("game4-screen-start").classList.add('active');
        document.getElementById("game4-layout-play").style.display = 'none';
        document.getElementById("game4-screen-end").style.display = 'none';
        return;
      }

      // Hide start screen, directly load play layout
      document.getElementById(gameId + "-screen-start").style.display = 'none';
      document.getElementById(gameId + "-screen-start").classList.remove('active');
      document.getElementById(gameId + "-layout-play").style.display = 'flex';
      document.getElementById(gameId + "-screen-end").style.display = 'none';

      // Show timer
      document.getElementById('global-timer-container').style.visibility = 'visible';
      startTimer();

      // Initialize based on saved states
      if (gameId === 'game1') {
        loadGame1Scenario();
      } else if (gameId === 'game2') {
        loadGame2Patient();
      } else if (gameId === 'game3') {
        if (state.game3.step === 1) {
          document.getElementById('game3-stage1-view').style.display = 'flex';
          document.getElementById('game3-stage2-view').style.display = 'none';
          document.getElementById('game3-left-progress').textContent = `剩餘重新設計機會：${2 - state.game3.retryCount} 次`;
          document.getElementById('game3-speech-text').textContent = "請點擊下方的活動，再點擊時間表中的格子，幫我安排暑假作息吧！";
          document.getElementById('game3-jelly-img').style.filter = "none";
          drawTimePie();
          loadGame3Timeline();
          setupGame3Selector();
          updateGame3Stats();
        } else {
          // If was mid-dashboard, just revert to layout step to avoid animation state bugs
          state.game3.step = 1;
          saveProgress();
          resumeActiveGame();
        }
      }
    }

    function initiateGame(gameId) {
      document.getElementById(gameId + "-screen-start").style.display = 'none';
      document.getElementById(gameId + "-screen-start").classList.remove('active');
      document.getElementById(gameId + "-layout-play").style.display = 'flex';

      // Start Timer
      state.timeLeft = 600; // 10 minutes
      document.getElementById('global-timer-container').style.visibility = 'visible';
      updateTimerText();
      startTimer();

      // Initialize game scenes
      if (gameId === 'game1') {
        state.game1.currentScenario = 0;
        state.game1.clickedSecrets = [];
        state.game1.step = 1;
        loadGame1Scenario();
      } else if (gameId === 'game2') {
        state.game2.currentPatient = 0;
        state.game2.step = 1;
        state.game2.selectedToxins = [];
        state.game2.slots = {};
        state.game2.redAlertCount = 0;
        loadGame2Patient();
      } else if (gameId === 'game3') {
        state.game3.timeline = Array(14).fill(null);
        state.game3.selectedActivityId = "eat";
        state.game3.retryCount = 0;
        state.game3.step = 1;
        
        // Reset UI
        document.getElementById('game3-stage1-view').style.display = 'flex';
        document.getElementById('game3-stage2-view').style.display = 'none';
        document.getElementById('game3-left-progress').textContent = "剩餘重新設計機會：2 次";
        document.getElementById('game3-speech-text').textContent = "請點擊下方的活動，再點擊時間表中的格子，幫我安排暑假作息吧！";
        document.getElementById('game3-jelly-img').style.filter = "none";
        
        drawTimePie();
        loadGame3Timeline();
        setupGame3Selector();
        updateGame3Stats();
      } else if (gameId === 'game4') {
        startGame4();
      }
      saveProgress();
    }

    function completeGameAndGoHome(gameId) {
      state.gamesCompleted[gameId] = true;
      state.activeGame = null;
      stopTimer();
      saveProgress();
      goHome();
      createConfetti();
    }

    // --- Timer System ---
    function startTimer() {
      stopTimer();
      timerInterval = setInterval(() => {
        state.timeLeft--;
        updateTimerText();
        if (state.timeLeft <= 0) {
          stopTimer();
          handleTimeOut();
        }
        // Save time state
        if (state.timeLeft % 5 === 0) {
          saveProgress();
        }
      }, 1000);
    }

    function stopTimer() {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
      }
    }

    function updateTimerText() {
      const min = Math.floor(state.timeLeft / 60);
      const sec = state.timeLeft % 60;
      const displayMin = min < 10 ? '0' + min : min;
      const displaySec = sec < 10 ? '0' + sec : sec;
      const timerText = document.getElementById('global-timer-text');
      const timerContainer = document.getElementById('global-timer-container');
      
      timerText.textContent = "⏳ " + displayMin + ":" + displaySec;

      // Flashing alert at last 30s
      if (state.timeLeft <= 30) {
        timerContainer.classList.add('timer-flash');
      } else {
        timerContainer.classList.remove('timer-flash');
      }
    }

    function handleTimeOut() {
      stopTimer();
      const gameId = state.activeGame;
      if (!gameId) return;

      showModal("⏰ 時間到囉！很可惜，果凍人需要你更快的幫助！要再試一次嗎？", "⏱️", "retry", () => {
        initiateGame(gameId);
      });
    }

    // --- Game 1: 網路交友偵探 logic ---
    function loadGame1Scenario() {
      const scenarioIndex = state.game1.currentScenario;
      if (scenarioIndex >= game1Scenarios.length) {
        // End game
        showGame1EndScreen();
        return;
      }

      const data = game1Scenarios[scenarioIndex];
      document.getElementById('game1-header-title').textContent = data.title;
      document.getElementById('game1-left-progress').textContent = "進度：情境 " + (scenarioIndex + 1) + " / " + game1Scenarios.length;

      // Set character text
      if (state.game1.step === 1) {
        document.getElementById('game1-speech-text').textContent = "請在左邊的聊天室中，找出看起來奇怪或危險的對話點點看！";
        document.getElementById('game1-step-indicator').textContent = "步驟 1：點選危險句子";
        document.getElementById('game1-instruction-panel').style.display = 'flex';
        document.getElementById('game1-mc-panel').style.display = 'none';
        document.getElementById('game1-mc-panel').classList.remove('active');
      } else {
        document.getElementById('game1-speech-text').textContent = "你成功找出了危險訊號！那我們現在應該怎麼做呢？";
        document.getElementById('game1-step-indicator').textContent = "步驟 2：選擇正確做法";
        document.getElementById('game1-instruction-panel').style.display = 'none';
        document.getElementById('game1-mc-panel').style.display = 'flex';
        document.getElementById('game1-mc-panel').classList.add('active');
        setupGame1MC();
      }

      // Populate chat bubble logs
      const chatContainer = document.getElementById('game1-chat-container');
      chatContainer.innerHTML = '';

      data.messages.forEach(msg => {
        const div = document.createElement('div');
        div.className = "chat-bubble " + msg.sender;
        div.innerHTML = msg.text;
        chatContainer.appendChild(div);
      });

      // Attach clicks to dangerous phrases
      const dangerPhrases = chatContainer.querySelectorAll('.danger-phrase');
      dangerPhrases.forEach(el => {
        const phraseId = el.getAttribute('data-id');
        
        // Restore clicked state from storage if any
        if (state.game1.clickedSecrets.includes(phraseId)) {
          el.classList.add('detected');
        }

        el.addEventListener('click', (e) => {
          if (state.game1.step !== 1) return; // Only clickable in step 1
          
          if (!el.classList.contains('detected')) {
            el.classList.add('detected');
            state.game1.clickedSecrets.push(phraseId);
            saveProgress();
            
            // Shatter/Pop visual particles
            createShatterParticles(el);
            
            // Check if all secrets are found
            if (state.game1.clickedSecrets.length === data.dangerCount) {
              setTimeout(() => {
                showSuccessPopup("發現危險訊號！🚨", "你太棒了！抓出網友說的可疑句子了。接下來請選擇應對方式！", () => {
                  state.game1.step = 2;
                  saveProgress();
                  loadGame1Scenario();
                });
              }, 600);
            }
          }
        });
      });
    }

    function setupGame1MC() {
      const scenarioIndex = state.game1.currentScenario;
      const data = game1Scenarios[scenarioIndex];
      const mcOptions = document.getElementById('game1-mc-options');
      mcOptions.innerHTML = '';

      document.getElementById('game1-mc-question').textContent = data.question;

      data.options.forEach((opt, idx) => {
        const btn = document.createElement('div');
        btn.className = 'mc-option';
        btn.textContent = opt.label;
        btn.addEventListener('click', () => {
          if (opt.isCorrect) {
            showModal("👍 答對了！\\n\\n" + opt.feedback, "🎉", "success", () => {
              // Move to next scenario
              state.game1.currentScenario++;
              state.game1.clickedSecrets = [];
              state.game1.step = 1;
              saveProgress();
              loadGame1Scenario();
              createConfetti();
            });
          } else {
            // Add shake animation to card
            btn.classList.add('shake-animation');
            setTimeout(() => btn.classList.remove('shake-animation'), 400);
            showModal("❌ 再想想看喔！\\n\\n" + opt.feedback, "🤔", "retry");
          }
        });
        mcOptions.appendChild(btn);
      });
    }

    function showGame1EndScreen() {
      document.getElementById('game1-layout-play').style.display = 'none';
      document.getElementById('game1-screen-end').style.display = 'flex';
      document.getElementById('game1-screen-end').classList.add('active');
      document.getElementById('global-timer-container').style.visibility = 'hidden';
      stopTimer();
    }

    // --- Game 2: 留言急診室 logic ---
    function loadGame2Patient() {
      const patientIndex = state.game2.currentPatient;
      if (patientIndex >= game2Patients.length) {
        showGame2EndScreen();
        return;
      }

      const data = game2Patients[patientIndex];
      document.getElementById('game2-patient-name').textContent = data.name;
      document.getElementById('game2-post-text').textContent = data.post;
      document.getElementById('game2-left-progress').textContent = "病患：" + (patientIndex + 1) + " / " + game2Patients.length;

      // Set initial health bar based on step
      const healthFill = document.getElementById('game2-health-fill');
      const healthText = document.getElementById('game2-health-text');
      const healthEmoji = document.getElementById('game2-health-emoji');

      if (state.game2.step === 1) {
        healthFill.style.width = '20%';
        healthFill.style.backgroundColor = 'var(--primary-red)';
        healthText.textContent = '20%';
        healthEmoji.textContent = '😢';
        document.getElementById('game2-instruction-bar').textContent = "第一步：找出毒素！請點擊留言中「傷人、嘲笑」的字詞，把毒素消滅。";
        document.getElementById('game2-speech-text').textContent = "這些評論讓人好難過⋯請幫我點擊選取那些傷人的詞語！選取後會變淡喔！";
        document.getElementById('game2-antidotes-box').style.display = 'none';
        document.getElementById('game2-antidotes-box').classList.remove('active');
        document.getElementById('game2-btn-submit').textContent = "🩺 去毒完畢，進行下一步";
      } else {
        healthFill.style.width = '50%';
        healthFill.style.backgroundColor = 'var(--primary-orange)';
        healthText.textContent = '50%';
        healthEmoji.textContent = '😐';
        document.getElementById('game2-instruction-bar').textContent = "第二步：填入解藥！請將下方綠色的溫暖詞語填入對話的空白框中。";
        document.getElementById('game2-speech-text').textContent = "毒素被清除了！現在請拖曳或點擊底下的藥劑泡泡，填補對話中的空格！";
        document.getElementById('game2-antidotes-box').style.display = 'flex';
        document.getElementById('game2-antidotes-box').classList.add('active');
        document.getElementById('game2-btn-submit').textContent = "🩺 送出診斷並檢查";
        setupGame2Antidotes();
      }

      setupGame2CommentBlocks();
    }

    function setupGame2CommentBlocks() {
      const patientIndex = state.game2.currentPatient;
      const data = game2Patients[patientIndex];
      const container = document.getElementById('game2-words-container');
      container.innerHTML = '';

      if (state.game2.step === 1) {
        // Step 1: Render toxic and non-toxic words
        data.rawWords.forEach((word, idx) => {
          const isToxin = data.toxins.some(t => t.trim() === word.trim());
          const block = document.createElement('div');
          block.className = 'word-block';
          block.textContent = word;

          const isDeletedCandidate = state.game2.selectedToxins.includes(idx);
          if (isDeletedCandidate) {
            block.classList.add('deleted-candidate');
          }

          block.addEventListener('click', () => {
            // Toggle deleted-candidate state
            if (state.game2.selectedToxins.includes(idx)) {
              const findIdx = state.game2.selectedToxins.indexOf(idx);
              state.game2.selectedToxins.splice(findIdx, 1);
              block.classList.remove('deleted-candidate');
            } else {
              state.game2.selectedToxins.push(idx);
              block.classList.add('deleted-candidate');
              
              if (isToxin) {
                createShatterParticles(block);
              } else {
                // Non-toxin shake feedback, but still allow deletion
                block.classList.add('shake-animation');
                setTimeout(() => block.classList.remove('shake-animation'), 400);
              }
            }
            saveProgress();
          });

          container.appendChild(block);
        });
      } else {
        // Step 2: Render sentence template parts and slots, completely removing the original comment fragments!
        for (let i = 0; i < data.templateParts.length; i++) {
          // Add text part
          const textSpan = document.createElement('span');
          textSpan.textContent = data.templateParts[i];
          textSpan.style.fontSize = '20px';
          textSpan.style.fontWeight = '800';
          container.appendChild(textSpan);

          // Add slot if not the last part
          if (i < data.templateParts.length - 1) {
            const slotIdx = i;
            const slot = document.createElement('div');
            slot.className = 'word-slot';
            slot.setAttribute('data-slot-id', slotIdx);
            
            // If already filled
            const filledWord = state.game2.slots[slotIdx];
            if (filledWord) {
              slot.textContent = filledWord;
              slot.classList.add('filled');
            } else {
              slot.textContent = "空格 " + (slotIdx + 1);
            }

            // Click slot to clear it
            slot.addEventListener('click', () => {
              if (slot.classList.contains('filled')) {
                const wordToFree = state.game2.slots[slotIdx];
                delete state.game2.slots[slotIdx];
                saveProgress();
                
                // Return bubble to pool
                const bubbles = document.querySelectorAll('.antidote-bubble');
                bubbles.forEach(b => {
                  if (b.textContent === wordToFree) {
                    b.classList.remove('used');
                  }
                });

                loadGame2Patient();
              }
            });

            // Setup drop receiver for Pointer Events
            slot.addEventListener('pointerenter', () => slot.style.background = '#E6F0FA');
            slot.addEventListener('pointerleave', () => slot.style.background = '');

            container.appendChild(slot);
          }
        }
      }
    }

    function setupGame2Antidotes() {
      const patientIndex = state.game2.currentPatient;
      const data = game2Patients[patientIndex];
      const container = document.getElementById('game2-antidote-bubbles');
      container.innerHTML = '';

      // Combine and shuffle good and bad antidotes
      const allBubbles = [...data.goodAntidotes, ...data.badAntidotes];
      allBubbles.sort(); // Consistent order

      allBubbles.forEach(word => {
        const b = document.createElement('div');
        b.className = 'antidote-bubble';
        b.textContent = word;

        // If currently in slot, mark used
        const isUsed = Object.values(state.game2.slots).includes(word);
        if (isUsed) {
          b.classList.add('used');
        }

        // Handle Tap-to-select (fallback)
        b.addEventListener('click', () => {
          if (b.classList.contains('used')) return;
          
          // Find first empty slot
          const slotCount = data.templateParts.length - 1;
          let targetSlot = -1;
          for (let i = 0; i < slotCount; i++) {
            if (!state.game2.slots[i]) {
              targetSlot = i;
              break;
            }
          }

          if (targetSlot !== -1) {
            state.game2.slots[targetSlot] = word;
            b.classList.add('used');
            saveProgress();
            loadGame2Patient();
          } else {
            showModal("空格都填滿囉！你可以先點擊對話框裡的詞語來清空它喔。", "💡", "retry");
          }
        });

        // Setup dragging via Pointer Events
        setupPointerDrag(b, word);

        container.appendChild(b);
      });
    }

    // Modern pointer drag-and-drop system
    function setupPointerDrag(element, word) {
      let startX = 0;
      let startY = 0;
      let originalX = 0;
      let originalY = 0;
      let isDragging = false;
      let dragClone = null;

      element.addEventListener('pointerdown', (e) => {
        if (element.classList.contains('used')) return;
        
        element.setPointerCapture(e.pointerId);
        const rect = element.getBoundingClientRect();
        const containerRect = document.getElementById('app-container').getBoundingClientRect();
        
        startX = e.clientX;
        startY = e.clientY;
        originalX = rect.left - containerRect.left;
        originalY = rect.top - containerRect.top;

        isDragging = true;
        
        // Create dragging element
        dragClone = element.cloneNode(true);
        dragClone.className = 'antidote-bubble dragging';
        dragClone.style.left = originalX + 'px';
        dragClone.style.top = originalY + 'px';
        dragClone.style.width = rect.width + 'px';
        dragClone.style.height = rect.height + 'px';
        
        document.getElementById('app-container').appendChild(dragClone);
      });

      element.addEventListener('pointermove', (e) => {
        if (!isDragging || !dragClone) return;
        
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        
        dragClone.style.left = (originalX + dx) + 'px';
        dragClone.style.top = (originalY + dy) + 'px';
      });

      element.addEventListener('pointerup', (e) => {
        if (!isDragging) return;
        isDragging = false;
        element.releasePointerCapture(e.pointerId);

        if (dragClone) {
          // Find if overlapping with any word-slots
          const cloneRect = dragClone.getBoundingClientRect();
          const slots = document.querySelectorAll('.word-slot');
          let hitSlot = null;

          slots.forEach(slot => {
            const sRect = slot.getBoundingClientRect();
            // A simple bounding box check
            const overlap = !(cloneRect.right < sRect.left || 
                              cloneRect.left > sRect.right || 
                              cloneRect.bottom < sRect.top || 
                              cloneRect.top > sRect.bottom);
            if (overlap) {
              hitSlot = slot;
            }
          });

          dragClone.remove();
          dragClone = null;

          if (hitSlot) {
            const slotId = hitSlot.getAttribute('data-slot-id');
            // If already filled, free the old word
            const oldWord = state.game2.slots[slotId];
            if (oldWord) {
              const oldBubbles = document.querySelectorAll('.antidote-bubble');
              oldBubbles.forEach(ob => {
                if (ob.textContent === oldWord) ob.classList.remove('used');
              });
            }

            state.game2.slots[slotId] = word;
            element.classList.add('used');
            saveProgress();
            loadGame2Patient();
          }
        }
      });
    }

    function submitGame2Diagnosis() {
      const patientIndex = state.game2.currentPatient;
      const data = game2Patients[patientIndex];

      if (state.game2.step === 1) {
        // Step 1: Check if all toxic words have been selected to delete
        let toxinsLeft = [];
        data.rawWords.forEach((word, idx) => {
          const isToxin = data.toxins.some(t => t.trim() === word.trim());
          if (isToxin && !state.game2.selectedToxins.includes(idx)) {
            toxinsLeft.push(word);
          }
        });

        if (toxinsLeft.length > 0) {
          // Red alert count increment
          state.game2.redAlertCount = (state.game2.redAlertCount || 0) + 1;
          saveProgress();
          showModal("這樣說話還是會傷人喔！😟\\n\\n你保留了『" + toxinsLeft[0] + "』這個詞，看到的人會很難過。\\n請把傷人的字詞都找出來打碎吧！", "❌", "retry");
          return;
        }

        // Successfully went through Step 1, proceed to Step 2
        state.game2.step = 2;
        saveProgress();
        loadGame2Patient();
        return;
      }

      // Step 2: Check if all slots are filled
      const slotCount = data.templateParts.length - 1;
      let emptySlot = false;
      for (let i = 0; i < slotCount; i++) {
        if (!state.game2.slots[i]) {
          emptySlot = true;
          break;
        }
      }

      if (emptySlot) {
        showModal("診斷還沒有完成喔！請把所有的空格都填滿解藥詞彙。", "💊", "retry");
        return;
      }

      // Check for bad antidotes in slots
      let hasBadWord = false;
      let offendingWord = "";
      
      for (let i = 0; i < slotCount; i++) {
        const word = state.game2.slots[i];
        if (data.badAntidotes.includes(word)) {
          hasBadWord = true;
          offendingWord = word;
          break;
        }
      }

      if (hasBadWord) {
        // Red alert count increment
        state.game2.redAlertCount = (state.game2.redAlertCount || 0) + 1;
        saveProgress();
        showModal("這樣說話還是會傷人喔！😟\\n\\n你填入了『" + offendingWord + "』，這個詞語看到的人會很難過。\\n請換成其他更溫暖鼓勵的話語吧！", "❌", "retry");
      } else {
        // SUCCESS! Transition health bar to 100% and show happiness
        const healthFill = document.getElementById('game2-health-fill');
        const healthText = document.getElementById('game2-health-text');
        const healthEmoji = document.getElementById('game2-health-emoji');

        healthFill.style.width = '100%';
        healthFill.style.backgroundColor = 'var(--primary-green)';
        healthText.textContent = '100%';
        healthEmoji.textContent = '😊';
        document.getElementById('game2-speech-text').textContent = "哇！留言變得很溫馨，我現在感覺好多了，謝謝你的急救！";

        createConfetti();

        setTimeout(() => {
          showModal("✨ 急救成功！果凍人的笑容回來了！", "🎉", "success", () => {
            // Next patient
            state.game2.currentPatient++;
            state.game2.step = 1;
            state.game2.selectedToxins = [];
            state.game2.slots = {};
            saveProgress();
            loadGame2Patient();
          });
        }, 600);
      }
    }

    function showGame2EndScreen() {
      document.getElementById('game2-layout-play').style.display = 'none';
      document.getElementById('game2-screen-end').style.display = 'flex';
      document.getElementById('game2-screen-end').classList.add('active');
      document.getElementById('global-timer-container').style.visibility = 'hidden';
      stopTimer();

      // Determine badge based on redAlertCount
      const count = state.game2.redAlertCount || 0;
      let badgeName = "";
      let badgeColor = "";
      
      if (count === 0) {
        badgeName = "火眼金睛急診師 🏅";
        badgeColor = "var(--primary-green-dark)";
      } else if (count === 1) {
        badgeName = "認真學習急診師 🥈";
        badgeColor = "var(--primary-blue-dark)";
      } else {
        badgeName = "越挫越勇急診師 🥉";
        badgeColor = "var(--primary-orange-dark)";
      }
      
      const badgeTextEl = document.getElementById('game2-badge-text');
      badgeTextEl.innerHTML = "獲得徽章：<span style='color: " + badgeColor + "; font-size: 24px; font-weight: 900; background: #FFFFFF; border: 2px solid var(--border-color); padding: 4px 12px; border-radius: 10px; box-shadow: 2px 2px 0px var(--border-color); display: inline-block; margin-top: 8px;'>" + badgeName + "</span><br><span style='font-size: 15px; font-weight: 600; color: #7A7060; display: inline-block; margin-top: 10px;'>(你在急診過程中一共觸發了 " + count + " 次紅色警示)</span>";
    }

    // --- Game 3: 數位生活設計師 logic ---
    function drawTimePie() {
      const svg = document.getElementById('time-pie-svg');
      svg.innerHTML = '';
      const cx = 270;
      const cy = 270;
      const radius = 170;
      const innerRadius = 80;
      const labelRadius = 205;
      
      // Draw 24 hours (15 degrees each)
      for (let h = 0; h < 24; h++) {
        const startAngle = (h / 24) * 2 * Math.PI - Math.PI / 2;
        const endAngle = ((h + 1) / 24) * 2 * Math.PI - Math.PI / 2;
        const midAngle = startAngle + Math.PI / 24;
        
        const x1 = cx + radius * Math.cos(startAngle);
        const y1 = cy + radius * Math.sin(startAngle);
        const x2 = cx + radius * Math.cos(endAngle);
        const y2 = cy + radius * Math.sin(endAngle);
        
        const xi1 = cx + innerRadius * Math.cos(startAngle);
        const yi1 = cy + innerRadius * Math.sin(startAngle);
        const xi2 = cx + innerRadius * Math.cos(endAngle);
        const yi2 = cy + innerRadius * Math.sin(endAngle);
        
        const d = `M ${x1} ${y1} A ${radius} ${radius} 0 0 1 ${x2} ${y2} L ${xi2} ${yi2} A ${innerRadius} ${innerRadius} 0 0 0 ${xi1} ${yi1} Z`;
        
        const isSleep = (h >= 22 || h < 8);
        let color = '#FFFDF6';
        let activityText = "未安排";
        let emoji = "";
        
        if (isSleep) {
          color = '#4D3F65'; // Sleep dark purple
          activityText = "😴 睡覺 (已鎖定)";
          emoji = "😴";
        } else {
          const slotIndex = h - 8;
          const activity = state.game3.timeline[slotIndex];
          if (activity) {
            color = activity.color;
            activityText = activity.emoji + " " + activity.name;
            emoji = activity.emoji;
          }
        }
        
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", d);
        path.setAttribute("fill", color);
        path.setAttribute("stroke", "#3D362A");
        path.setAttribute("stroke-width", "1.5");
        path.setAttribute("class", "time-sector" + (isSleep ? " locked" : ""));
        
        path.onclick = () => {
          if (isSleep) {
            showModal("果凍人此時正在睡覺（晚上 10 點到隔天早上 8 點），已經鎖定不能修改喔！😴", "😴", "retry");
          } else {
            const slotIndex = h - 8;
            const selId = state.game3.selectedActivityId;
            const existing = state.game3.timeline[slotIndex];
            // Toggle-to-clear: clicking the same activity again clears the slot
            if (existing && selId && existing.id === selId) {
              state.game3.timeline[slotIndex] = null;
            } else if (selId === 'clear') {
              state.game3.timeline[slotIndex] = null;
            } else {
              const matched = game3Activities.find(x => x.id === selId);
              if (matched) {
                state.game3.timeline[slotIndex] = { ...matched };
              }
            }
            saveProgress();
            drawTimePie();
            updateGame3Stats();
          }
        };
        
        const title = document.createElementNS("http://www.w3.org/2000/svg", "title");
        const labelHour = h < 10 ? '0' + h : h;
        const nextHour = (h + 1) % 24;
        const labelNext = nextHour < 10 ? '0' + nextHour : nextHour;
        title.textContent = labelHour + ":00 - " + labelNext + ":00 : " + activityText;
        path.appendChild(title);
        
        svg.appendChild(path);
        
        if (emoji) {
          const rEmoji = 125;
          const xe = cx + rEmoji * Math.cos(midAngle);
          const ye = cy + rEmoji * Math.sin(midAngle);
          
          const textEmoji = document.createElementNS("http://www.w3.org/2000/svg", "text");
          textEmoji.setAttribute("x", xe);
          textEmoji.setAttribute("y", ye);
          textEmoji.setAttribute("text-anchor", "middle");
          textEmoji.setAttribute("dominant-baseline", "central");
          textEmoji.setAttribute("font-size", "18px");
          textEmoji.style.pointerEvents = "none";
          textEmoji.textContent = emoji;
          svg.appendChild(textEmoji);
        }
        
        let labelText = "";
        if (h === 0) labelText = "凌晨12點";
        else if (h >= 1 && h <= 5) labelText = "凌晨" + h + "點";
        else if (h >= 6 && h <= 11) labelText = "上午" + h + "點";
        else if (h === 12) labelText = "中午12點";
        else if (h >= 13 && h <= 17) labelText = "下午" + (h - 12) + "點";
        else if (h >= 18 && h <= 23) labelText = "晚上" + (h - 12) + "點";
        
        const xl = cx + labelRadius * Math.cos(midAngle);
        const yl = cy + labelRadius * Math.sin(midAngle);
        
        const textLabel = document.createElementNS("http://www.w3.org/2000/svg", "text");
        textLabel.setAttribute("x", xl);
        textLabel.setAttribute("y", yl);
        
        const cosVal = Math.cos(midAngle);
        if (cosVal > 0.2) {
          textLabel.setAttribute("text-anchor", "start");
        } else if (cosVal < -0.2) {
          textLabel.setAttribute("text-anchor", "end");
        } else {
          textLabel.setAttribute("text-anchor", "middle");
        }
        textLabel.setAttribute("dominant-baseline", "central");
        textLabel.setAttribute("font-size", "12px");
        textLabel.setAttribute("font-weight", "800");
        textLabel.setAttribute("fill", isSleep ? "#7A7060" : "#3D362A");
        textLabel.style.pointerEvents = "none";
        textLabel.textContent = labelText;
        svg.appendChild(textLabel);
      }
      
      const inner = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      inner.setAttribute("cx", cx);
      inner.setAttribute("cy", cy);
      inner.setAttribute("r", innerRadius);
      inner.setAttribute("fill", "#FFFDF6");
      inner.setAttribute("stroke", "#3D362A");
      inner.setAttribute("stroke-width", "3");
      inner.style.pointerEvents = "none";
      svg.appendChild(inner);
      
      const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
      txt.setAttribute("x", cx);
      txt.setAttribute("y", cy + 6);
      txt.setAttribute("text-anchor", "middle");
      txt.setAttribute("font-size", "16px");
      txt.setAttribute("font-weight", "900");
      txt.setAttribute("fill", "#3D362A");
      txt.style.pointerEvents = "none";
      txt.textContent = "暑假作息";
      svg.appendChild(txt);
    }

    function loadGame3Timeline() {
      // Stub: the timeline is now rendered directly inside the interactive SVG donut chart.
    }

    function setupGame3Selector() {
      const container = document.getElementById('game3-activity-selector');
      container.innerHTML = '';
      
      game3Activities.forEach(act => {
        const btn = document.createElement('button');
        btn.className = 'activity-btn';
        if (state.game3.selectedActivityId === act.id) {
          btn.classList.add('selected');
        }
        btn.style.backgroundColor = act.color;
        btn.innerHTML = "<span>" + act.emoji + "</span><span>" + act.name + "</span>";
        btn.onclick = () => {
          state.game3.selectedActivityId = act.id;
          setupGame3Selector();
        };
        container.appendChild(btn);
      });
    }

    function clearGame3Timeline() {
      state.game3.timeline = Array(14).fill(null);
      saveProgress();
      loadGame3Timeline();
      drawTimePie();
      updateGame3Stats();
    }

    function updateGame3Stats() {
      let screenHours = 0;
      let remainingHours = 0;
      
      for (let i = 0; i < 14; i++) {
        const act = state.game3.timeline[i];
        if (act) {
          if (act.id === 'screen') screenHours++;
        } else {
          remainingHours++;
        }
      }
      
      document.getElementById('game3-stat-screen').textContent = "📱 螢幕娛樂：" + screenHours + " 小時";
      document.getElementById('game3-stat-remaining').textContent = "⏳ 剩餘未安排：" + remainingHours + " 小時";
    }

    function submitGame3Timeline() {
      // Validate all 14 slots are filled
      const unfilled = state.game3.timeline.filter(x => !x).length;
      if (unfilled > 0) {
        showModal("還有 " + unfilled + " 個時間格沒有安排喔！請把所有格子都填滿再送出。📋", "📋", "retry");
        return;
      }

      // Transition step
      state.game3.step = 2;
      saveProgress();

      // Show stage 2 screen
      document.getElementById('game3-stage1-view').style.display = 'none';
      const stage2 = document.getElementById('game3-stage2-view');
      stage2.style.display = 'flex';
      
      const grid = document.getElementById('game3-indicators-grid');
      grid.innerHTML = '';
      
      const controls = document.getElementById('game3-stage2-controls');
      controls.innerHTML = '';

      // Perform checks
      // Sleep quality: check index 13 (21:00-22:00)
      const sleepBad = state.game3.timeline[13] && state.game3.timeline[13].id === 'screen';
      
      // Spirit state: total screen hours
      const screenHours = state.game3.timeline.filter(x => x && x.id === 'screen').length;
      let spiritState = "normal";
      if (screenHours > 6) spiritState = "bad";
      else if (screenHours <= 3) spiritState = "good";
      
      // Learn homework: at least one learn slot
      const hasLearn = state.game3.timeline.some(x => x && x.id === 'learn');
      
      // Family connection: at least one family slot
      const hasFamily = state.game3.timeline.some(x => x && x.id === 'family');

      const indicators = [
        {
          title: "睡眠品質",
          status: sleepBad ? "睡不好 ❌" : "睡得好 👍",
          color: sleepBad ? "var(--primary-red-dark)" : "var(--primary-green-dark)",
          text: sleepBad ? "滑手機滑到快睡著，但腦袋一直轉⋯" : "沒有在睡前看螢幕，睡得好香甜！",
          icon: sleepBad ? "🥱" : "😴",
          jellySpeech: sleepBad ? "滑手機滑到快睡著，但腦袋一直轉⋯" : "沒有在睡前看螢幕，睡得好香甜！",
          jellyFilter: sleepBad ? "grayscale(0.5) contrast(0.8)" : "none"
        },
        {
          title: "精神狀態",
          status: spiritState === "bad" ? "眼睛痠頭痛 ❌" : (spiritState === "good" ? "精神好 👍" : "普通 😐"),
          color: spiritState === "bad" ? "var(--primary-red-dark)" : (spiritState === "good" ? "var(--primary-green-dark)" : "var(--primary-orange-dark)"),
          text: spiritState === "bad" ? "眼睛超痠，頭有點痛⋯" : (spiritState === "good" ? "螢幕時間控制得很好，整天都有精神！" : "還算有精神，但眼睛有一點點疲倦喔。"),
          icon: spiritState === "bad" ? "🤕" : (spiritState === "good" ? "🤩" : "😐"),
          jellySpeech: spiritState === "bad" ? "眼睛超痠，頭有點痛⋯" : (spiritState === "good" ? "螢幕時間控制得很好，整天都有精神！" : "還算有精神，但眼睛有一點點疲倦喔。"),
          jellyFilter: spiritState === "bad" ? "hue-rotate(300deg) saturate(1.5)" : "none"
        },
        {
          title: "功課與學習",
          status: hasLearn ? "功課寫完了 👍" : "功課沒做 ❌",
          color: hasLearn ? "var(--primary-green-dark)" : "var(--primary-red-dark)",
          text: hasLearn ? "功課寫完了，輕鬆很多！" : "功課都沒做，明天開學怎麼辦⋯",
          icon: hasLearn ? "📚" : "😰",
          jellySpeech: hasLearn ? "功課寫完了，輕鬆很多！" : "功課都沒做，明天開學怎麼辦⋯",
          jellyFilter: hasLearn ? "none" : "grayscale(0.5)"
        },
        {
          title: "家人關係",
          status: hasFamily ? "關係好 👍" : "不理家人 ❌",
          color: hasFamily ? "var(--primary-green-dark)" : "var(--primary-red-dark)",
          text: hasFamily ? "跟家人一起吃飯好開心！" : "我整天都在房間，媽媽說我都不理她⋯",
          icon: hasFamily ? "👪" : "💔",
          jellySpeech: hasFamily ? "跟家人一起吃飯好開心！" : "我整天都在房間，媽媽說我都不理她⋯",
          jellyFilter: hasFamily ? "none" : "sepia(0.5)"
        }
      ];

      // Sequential pop in
      document.getElementById('game3-speech-text').textContent = "正在體驗新的一天⋯";
      
      indicators.forEach((ind, idx) => {
        setTimeout(() => {
          const card = document.createElement('div');
          card.className = 'indicator-card';
          card.innerHTML = `
            <div class='indicator-card-icon'>${ind.icon}</div>
            <div>
              <div style='font-size: 15px; font-weight: 800; color: #7A7060;'>${ind.title}</div>
              <div style='font-size: 18px; font-weight: 900; color: ${ind.color};'>${ind.status}</div>
              <div style='font-size: 14px; font-weight: 600; color: #5D5240; margin-top: 4px;'>${ind.text}</div>
            </div>
          `;
          grid.appendChild(card);
          
          // Trigger reflow & add class to slide in
          setTimeout(() => card.classList.add('visible'), 50);
          
          // Update character reaction
          const jellyImg = document.getElementById('game3-jelly-img');
          jellyImg.style.filter = ind.jellyFilter;
          document.getElementById('game3-speech-text').textContent = ind.jellySpeech;
          
          // Last indicator finished
          if (idx === indicators.length - 1) {
            setTimeout(() => {
              // Final summary word calculation
              let positiveCount = 0;
              if (!sleepBad) positiveCount++;
              if (spiritState === 'good') positiveCount++;
              if (hasLearn) positiveCount++;
              if (hasFamily) positiveCount++;
              
              let summaryText = "";
              let finalFilter = "none";
              
              if (positiveCount === 4) {
                summaryText = "哇！這是最完美的暑假生活！我過得非常充實又快樂，謝謝你！🌟";
                finalFilter = "none";
                createConfetti();
              } else if (positiveCount >= 2) {
                summaryText = "這個暑假生活還不錯，但有些地方如果能調整一下，我會更健康喔！😊";
                finalFilter = "none";
              } else {
                summaryText = "這個暑假好辛苦喔⋯我整天都在看螢幕，功課沒寫、頭又痛，我們重新設計看看好嗎？🥺";
                finalFilter = "grayscale(0.5)";
              }
              
              document.getElementById('game3-speech-text').textContent = summaryText;
              document.getElementById('game3-jelly-img').style.filter = finalFilter;
              
              renderStage2Controls();
            }, 800);
          }
          
        }, idx * 1000 + 500);
      });
    }

    function renderStage2Controls() {
      const container = document.getElementById('game3-stage2-controls');
      container.innerHTML = '';
      
      const retryCount = state.game3.retryCount || 0;
      
      if (retryCount < 2) {
        const btnRetry = document.createElement('button');
        btnRetry.className = 'btn-start-game';
        btnRetry.style.background = 'var(--primary-orange)';
        btnRetry.style.fontSize = '18px';
        btnRetry.style.height = '48px';
        btnRetry.textContent = "重新設計 (剩餘 " + (2 - retryCount) + " 次)";
        btnRetry.onclick = () => {
          state.game3.retryCount++;
          state.game3.step = 1;
          saveProgress();
          
          document.getElementById('game3-stage1-view').style.display = 'flex';
          document.getElementById('game3-stage2-view').style.display = 'none';
          document.getElementById('game3-left-progress').textContent = "剩餘重新設計機會：" + (2 - state.game3.retryCount) + " 次";
          document.getElementById('game3-speech-text').textContent = "請點擊下方的活動，再點擊時間表中的格子，幫我安排暑假作息吧！";
          document.getElementById('game3-jelly-img').style.filter = "none";
          
          drawTimePie();
          loadGame3Timeline();
        };
        container.appendChild(btnRetry);
      }
      
      const btnFinal = document.createElement('button');
      btnFinal.className = 'btn-start-game';
      btnFinal.style.background = 'var(--primary-blue)';
      btnFinal.style.fontSize = '18px';
      btnFinal.style.height = '48px';
      btnFinal.textContent = retryCount < 2 ? "前往結算" : "完成設計，前往結算";
      btnFinal.onclick = () => {
        showGame3EndScreen();
      };
      container.appendChild(btnFinal);
    }

    function showGame3EndScreen() {
      document.getElementById('game3-layout-play').style.display = 'none';
      document.getElementById('game3-screen-end').style.display = 'flex';
      document.getElementById('game3-screen-end').classList.add('active');
      document.getElementById('global-timer-container').style.visibility = 'hidden';
      stopTimer();

      const screenHours = state.game3.timeline.filter(x => x && x.id === 'screen').length;
      
      let feedback = "";
      let titleColor = "";
      if (screenHours <= 1) {
        feedback = "設計得很均衡！果凍人很感謝你 🌟";
        titleColor = "var(--primary-green-dark)";
      } else if (screenHours === 2) {
        feedback = "不錯，再調整一下會更好 👍";
        titleColor = "var(--primary-blue-dark)";
      } else {
        feedback = "果凍人有點辛苦，試試看少一點螢幕時間 😅";
        titleColor = "var(--primary-orange-dark)";
      }

      document.getElementById('game3-summary-title').textContent = "設計完成！";
      document.getElementById('game3-summary-score').innerHTML = "果凍人的暑假螢幕時間為：<span style='color: " + titleColor + "; font-size: 24px; font-weight: 900;'>" + screenHours + " 小時</span><br><br><span style='font-size: 20px; font-weight: 800; color: #5D5240;'>" + feedback + "</span>";
    }

    // --- Shatter Particle System ---
    function createShatterParticles(element) {
      const rect = element.getBoundingClientRect();
      const container = document.getElementById('app-container');
      const containerRect = container.getBoundingClientRect();
      
      const x = rect.left - containerRect.left + rect.width / 2;
      const y = rect.top - containerRect.top + rect.height / 2;

      for (let i = 0; i < 15; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        p.style.backgroundColor = i % 2 === 0 ? 'var(--primary-pink)' : 'var(--primary-orange)';
        p.style.left = x + 'px';
        p.style.top = y + 'px';

        const angle = Math.random() * Math.PI * 2;
        const distance = 30 + Math.random() * 60;
        const tx = Math.cos(angle) * distance;
        const ty = Math.sin(angle) * distance;

        p.style.setProperty('--tx', tx + 'px');
        p.style.setProperty('--ty', ty + 'px');

        container.appendChild(p);
        
        // Remove after animation finishes
        setTimeout(() => p.remove(), 600);
      }
    }

    // --- Confetti System ---
    function createConfetti() {
      const container = document.getElementById('app-container');
      const colors = ['#5D9CEC', '#F0965A', '#F6C4C8', '#A7DCA8', '#FFCE54'];
      
      for (let i = 0; i < 50; i++) {
        const c = document.createElement('div');
        c.className = 'confetti';
        c.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        c.style.left = (Math.random() * 100) + '%';
        c.style.top = '-20px';
        c.style.width = (8 + Math.random() * 8) + 'px';
        c.style.height = (16 + Math.random() * 12) + 'px';

        const rotation = Math.random() * 360;
        const duration = 1.8 + Math.random() * 1.5;
        const delay = Math.random() * 0.4;

        c.style.animation = "fall-animation " + duration + "s linear " + delay + "s forwards";
        c.style.transform = "rotate(" + rotation + "deg)";

        container.appendChild(c);
        setTimeout(() => c.remove(), (duration + delay) * 1000);
      }
    }

    // --- Custom Modal Alert System ---
    let activeModalCallback = null;

    function showModal(desc, icon, type, callback) {
      if (icon === undefined) icon = '❌';
      if (type === undefined) type = 'retry';
      if (callback === undefined) callback = null;

      const overlay = document.getElementById('custom-modal');
      const titleEl = document.getElementById('modal-title');
      const descEl = document.getElementById('modal-desc');
      const iconEl = document.getElementById('modal-icon');
      const btnEl = document.getElementById('modal-btn-close');

      descEl.innerHTML = desc.replace(/\\n/g, '<br>');
      iconEl.textContent = icon;
      activeModalCallback = callback;

      if (type === 'success') {
        titleEl.textContent = '太棒了！';
        titleEl.style.color = 'var(--primary-green-dark)';
        btnEl.textContent = '繼續';
        btnEl.className = 'btn-modal-close success';
      } else if (type === 'retry') {
        titleEl.textContent = '注意！';
        titleEl.style.color = 'var(--primary-red-dark)';
        btnEl.textContent = '確認';
        btnEl.className = 'btn-modal-close retry';
      } else {
        titleEl.textContent = '通知';
        titleEl.style.color = 'var(--border-color)';
        btnEl.textContent = '好';
        btnEl.className = 'btn-modal-close';
      }

      overlay.style.display = 'flex';
      overlay.classList.add('active');
    }

    function showConfirmModal(desc, callback) {
      showModal(desc, '⚠️', 'retry', callback);
      const btnEl = document.getElementById('modal-btn-close');
      btnEl.textContent = '確認清除';
    }

    function showSuccessPopup(title, desc, callback) {
      showModal(desc, '🎉', 'success', callback);
      document.getElementById('modal-title').textContent = title;
    }

    function closeModal() {
      const overlay = document.getElementById('custom-modal');
      if (overlay) {
        overlay.style.display = 'none';
        overlay.classList.remove('active');
      }
      if (activeModalCallback) {
        const cb = activeModalCallback;
        activeModalCallback = null;
        cb();
      }
    }

    // --- Google Sheets & Teacher Settings ---
    function saveStudentName(val) {
      state.studentName = val.trim();
      saveProgress();
    }

    function openTeacherSettings() {
      const modal = document.getElementById('teacher-settings-modal');
      const input = document.getElementById('gas-url-input');
      const codeInput = document.getElementById('gas-code-input');
      const textarea = document.getElementById('gas-code-textarea');
      
      input.value = state.googleAppScriptUrl || "";
      if (codeInput) {
        codeInput.value = state.googleAppScriptCode || "";
      }
      
      textarea.value = `function doPost(e) {\n  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();\n  var data;\n  try {\n    data = JSON.parse(e.postData.contents);\n  } catch(err) {\n    return ContentService.createTextOutput(JSON.stringify({"status": "error", "message": err.message}))\n      .setMimeType(ContentService.MimeType.JSON);\n  }\n  \n  if (sheet.getLastRow() === 0) {\n    sheet.appendRow(["提交時間", "姓名/座號", "剩餘時間(秒)", "遊戲一完成", "遊戲二紅訊次數", "遊戲三螢幕時間", "打地鼠測驗分數"]);\n  }\n  \n  sheet.appendRow([\n    new Date(),\n    data.studentName,\n    data.timeLeft,\n    data.game1Completed ? "已完成" : "未完成",\n    data.game2RedAlertCount,\n    data.game3ScreenHours + "小時",\n    data.game4Score + "分"\n  ]);\n  \n  return ContentService.createTextOutput(JSON.stringify({"status": "success"}))\n    .setMimeType(ContentService.MimeType.JSON);\n}`;
      
      modal.style.display = 'flex';
      modal.classList.add('active');
    }

    function closeTeacherSettings() {
      const modal = document.getElementById('teacher-settings-modal');
      modal.style.display = 'none';
      modal.classList.remove('active');
    }

    function generateRandomConnectionCode() {
      let code = "";
      for (let i = 0; i < 6; i++) {
        code += Math.floor(Math.random() * 10);
      }
      const codeInput = document.getElementById('gas-code-input');
      if (codeInput) codeInput.value = code;
    }

    function saveTeacherSettings() {
      const input = document.getElementById('gas-url-input');
      const codeInput = document.getElementById('gas-code-input');
      const urlVal = input.value.trim();
      const codeVal = codeInput ? codeInput.value.trim() : "";
      
      if (codeVal && !/^\d{6}$/.test(codeVal)) {
        showModal("連接碼必須為 6 位數字！", "❌", "error");
        return;
      }
      
      state.googleAppScriptUrl = urlVal;
      state.googleAppScriptCode = codeVal;
      saveProgress();
      
      if (codeVal && urlVal) {
        fetch(`https://kvs.ix.workers.dev/lingproject_cybersecurity_pwa_v1/${codeVal}`, {
          method: 'PUT',
          body: urlVal
        })
        .then(res => {
          if (!res.ok) throw new Error("KV upload failed");
          console.log("KV upload successful for code:", codeVal);
        })
        .catch(err => {
          console.error("無法同步代碼至雲端：", err);
        });
      }
      
      closeTeacherSettings();
      updateConnectionUI();
      showSuccessPopup("儲存成功", "後台網址已成功儲存！當學生完成最後的打地鼠測驗時，系統將自動上傳成績至您的 Google 試算表。");
    }

    function handleStudentCodeInput(val) {
      const cleanVal = val.trim();
      if (cleanVal.length === 6) {
        if (!/^\d{6}$/.test(cleanVal)) {
          updateConnectionStatus("❌ 格式應為6位數字", "var(--primary-red-dark)");
          return;
        }
        
        updateConnectionStatus("⏳ 正在連線...", "var(--primary-orange-dark)");
        
        fetch(`https://kvs.ix.workers.dev/lingproject_cybersecurity_pwa_v1/${cleanVal}`)
          .then(res => {
            if (!res.ok) {
              if (res.status === 404) {
                throw new Error("無效的連接碼");
              }
              throw new Error("伺服器連線失敗");
            }
            return res.text();
          })
          .then(url => {
            const trimmedUrl = url.trim();
            if (trimmedUrl.startsWith("https://script.google.com/")) {
              state.googleAppScriptUrl = trimmedUrl;
              state.googleAppScriptCode = cleanVal;
              saveProgress();
              updateConnectionUI();
              showModal("🎉 成功連接至教師後台試算表！", "✨", "success");
            } else {
              throw new Error("讀取網址錯誤");
            }
          })
          .catch(err => {
            console.error("連接錯誤：", err);
            updateConnectionStatus("❌ 連接碼無效", "var(--primary-red-dark)");
            state.googleAppScriptUrl = "";
            state.googleAppScriptCode = "";
            saveProgress();
            const linkedLbl = document.getElementById('student-linked-url-lbl');
            if (linkedLbl) linkedLbl.textContent = "";
          });
      } else {
        if (cleanVal.length === 0) {
          state.googleAppScriptUrl = "";
          state.googleAppScriptCode = "";
          saveProgress();
          updateConnectionUI();
        } else {
          updateConnectionStatus("請輸入 6 位數字...", "#7A7060");
        }
      }
    }

    function updateConnectionUI() {
      const codeInput = document.getElementById('student-code-input');
      const statusText = document.getElementById('connection-status-text');
      const linkedLbl = document.getElementById('student-linked-url-lbl');
      
      if (codeInput) {
        codeInput.value = state.googleAppScriptCode || "";
      }
      
      if (state.googleAppScriptUrl && state.googleAppScriptUrl.startsWith("https://script.google.com/")) {
        if (statusText) {
          statusText.textContent = "✅ 已連接";
          statusText.style.color = "var(--primary-green-dark)";
        }
        if (linkedLbl) {
          if (state.googleAppScriptCode) {
            linkedLbl.textContent = "🔗 已綁定代碼：" + state.googleAppScriptCode;
          } else {
            linkedLbl.textContent = "🔗 已手動綁定後台網址";
          }
        }
      } else {
        if (statusText) {
          statusText.textContent = "未連接";
          statusText.style.color = "#7A7060";
        }
        if (linkedLbl) {
          linkedLbl.textContent = "";
        }
      }
    }

    function updateConnectionStatus(text, color) {
      const statusText = document.getElementById('connection-status-text');
      if (statusText) {
        statusText.textContent = text;
        statusText.style.color = color;
      }
    }

    function copyGasCode() {
      const textarea = document.getElementById('gas-code-textarea');
      textarea.select();
      document.execCommand('copy');
      alert('程式碼已複製到剪貼簿！');
    }

    function clickGame4Card() {
      if (!state.gamesCompleted.game1 || !state.gamesCompleted.game2 || !state.gamesCompleted.game3) {
        showModal("請先通關前面三個關卡，即可解鎖綜合測驗打地鼠！🔒", "🔒", "retry");
        return;
      }
      startGameFlow('game4');
    }

    // --- Game 4 (Whack-a-Mole) Logic ---
    let game4ActiveMoles = Array(9).fill(null);
    let game4TimerInterval = null;
    let game4SpawnInterval = null;
    let game4Score = 0;
    let game4TimeLeft = 60;

    function startGame4() {
      document.getElementById('game4-screen-start').style.display = 'none';
      document.getElementById('game4-layout-play').style.display = 'flex';
      document.getElementById('game4-screen-end').style.display = 'none';

      game4Score = 0;
      game4TimeLeft = 60;
      game4ActiveMoles.fill(null);
      
      document.getElementById('game4-score-display').textContent = "0 分";
      document.getElementById('game4-time-display').textContent = "60 秒";
      
      for (let i = 0; i < 9; i++) {
        const mole = document.getElementById('mole-' + i);
        mole.classList.remove('up');
        mole.classList.remove('whacked');
        mole.style.backgroundColor = '';
      }

      // Start quiz timer
      game4TimerInterval = setInterval(() => {
        game4TimeLeft--;
        document.getElementById('game4-time-display').textContent = game4TimeLeft + " 秒";
        
        if (game4TimeLeft <= 0) {
          endGame4();
        }
      }, 1000);

      // Mole spawn timer
      game4SpawnInterval = setInterval(() => {
        const countToSpawn = Math.random() > 0.6 ? 2 : 1;
        for (let k = 0; k < countToSpawn; k++) {
          spawnMole();
        }
      }, 1100);
    }

    function hideMole(index) {
      const mole = document.getElementById('mole-' + index);
      if (mole) mole.classList.remove('up');
      game4ActiveMoles[index] = null;
    }

    // Expose hideMole globally so goHome() can safely call it
    window.hideMole = hideMole;

    function spawnMole() {
      const emptyHoles = [];
      for (let i = 0; i < 9; i++) {
        if (!game4ActiveMoles[i]) {
          emptyHoles.push(i);
        }
      }

      if (emptyHoles.length === 0) return;
      const holeIndex = emptyHoles[Math.floor(Math.random() * emptyHoles.length)];
      const statement = moleStatements[Math.floor(Math.random() * moleStatements.length)];

      const mole = document.getElementById('mole-' + holeIndex);
      const sign = document.getElementById('mole-sign-' + holeIndex);
      
      sign.textContent = statement.text;
      mole.style.backgroundColor = '#C67844';
      mole.classList.add('up');
      mole.classList.remove('whacked');

      const timeoutId = setTimeout(() => {
        hideMole(holeIndex);
      }, 2400);

      game4ActiveMoles[holeIndex] = {
        isCorrect: statement.isCorrect,
        timeoutId: timeoutId
      };
    }

    function whackMole(index) {
      const active = game4ActiveMoles[index];
      if (!active) return;
      
      const mole = document.getElementById('mole-' + index);
      if (mole.classList.contains('whacked')) return;
      mole.classList.add('whacked');

      clearTimeout(active.timeoutId);

      const isCorrect = active.isCorrect;
      if (isCorrect) {
        game4Score++;
        mole.style.backgroundColor = '#A0D28E';
        playBeep(600, 150);
        showFloatingText(mole, "+1");
      } else {
        game4Score--;
        mole.style.backgroundColor = '#E74C3C';
        playBeep(220, 300);
        showFloatingText(mole, "-1");
      }

      document.getElementById('game4-score-display').textContent = game4Score + " 分";

      setTimeout(() => {
        hideMole(index);
      }, 500);
    }

    function showFloatingText(element, text) {
      const rect = element.getBoundingClientRect();
      const container = document.getElementById('app-container');
      const containerRect = container.getBoundingClientRect();
      
      const x = rect.left - containerRect.left + rect.width / 2;
      const y = rect.top - containerRect.top;

      const floatText = document.createElement('div');
      floatText.textContent = text;
      floatText.style.position = 'absolute';
      floatText.style.left = x + 'px';
      floatText.style.top = y + 'px';
      floatText.style.fontSize = '24px';
      floatText.style.fontWeight = '900';
      floatText.style.color = text.startsWith('+') ? '#27AE60' : '#C0392B';
      floatText.style.textShadow = '2px 2px 0px #FFF';
      floatText.style.pointerEvents = 'none';
      floatText.style.zIndex = '999';
      floatText.style.transition = 'all 0.8s ease-out';
      
      container.appendChild(floatText);

      setTimeout(() => {
        floatText.style.transform = 'translateY(-50px)';
        floatText.style.opacity = '0';
      }, 50);

      setTimeout(() => {
        floatText.remove();
      }, 900);
    }

    function playBeep(freq, duration) {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();

        oscillator.type = 'sine';
        oscillator.frequency.value = freq;
        
        gainNode.gain.setValueAtTime(0.12, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration / 1000);
        
        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + duration / 1000);
      } catch (e) {
        console.warn("Web Audio API warning:", e);
      }
    }

    function endGame4() {
      clearInterval(game4TimerInterval);
      clearInterval(game4SpawnInterval);
      
      for (let i = 0; i < 9; i++) {
        if (game4ActiveMoles[i]) clearTimeout(game4ActiveMoles[i].timeoutId);
        hideMole(i);
      }

      document.getElementById('game4-layout-play').style.display = 'none';
      document.getElementById('game4-screen-end').style.display = 'flex';
      document.getElementById('game4-screen-end').classList.add('active');

      state.gamesCompleted.game4 = true;
      
      if (typeof state.game4BestScore === 'undefined') {
        state.game4BestScore = 0;
      }
      if (game4Score > state.game4BestScore) {
        state.game4BestScore = game4Score;
      }
      saveProgress();

      let badge = "再接再厲 📝";
      if (state.game4BestScore >= 24) {
        badge = "資安小達人 👑";
      } else if (state.game4BestScore >= 12) {
        badge = "資安守護者 🛡️";
      }

      document.getElementById('game4-summary-score').innerHTML = "你的本次得分為：<span style='color: var(--primary-green-dark); font-size: 32px; font-weight: 900;'>" + game4Score + " 分</span><br>歷史最佳得分：<span style='color: var(--primary-blue-dark); font-size: 24px; font-weight: 800;'>" + state.game4BestScore + " 分</span><br><br><span style='font-size: 20px; font-weight: 800; color: #5D5240;'>獲得稱號：" + badge + "</span>";

      // Upload scores to Google Sheet
      const url = state.googleAppScriptUrl || "";
      const statusEl = document.getElementById('game4-upload-status');
      
      if (!url) {
        statusEl.textContent = "⚠️ 教師後台網址未設定，成績僅保存在本地瀏覽器。";
        statusEl.style.color = 'var(--primary-orange-dark)';
      } else {
        statusEl.textContent = "⏳ 正在自動將成績上傳至 Google 試算表...";
        statusEl.style.color = '#7A7060';

        const payload = {
          studentName: state.studentName,
          timeLeft: state.timeLeft,
          game1Completed: state.gamesCompleted.game1,
          game2RedAlertCount: state.game2.redAlertCount || 0,
          game3ScreenHours: state.game3.timeline.filter(x => x && x.id === 'screen').length,
          game4Score: state.game4BestScore,
          progressPercent: 100
        };

        fetch(url, {
          method: 'POST',
          mode: 'no-cors',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })
        .then(() => {
          statusEl.textContent = "✅ 成績已成功上傳至 Google 試算表！";
          statusEl.style.color = 'var(--primary-green-dark)';
        })
        .catch(err => {
          console.error("Upload error:", err);
          statusEl.textContent = "❌ 上傳失敗，請檢查網路連線或後台網址設定。";
          statusEl.style.color = 'var(--primary-red-dark)';
        });
      }
    }
  </script>
</body>
</html>
""".replace('{jelly_base64}', jelly_base64)

# Write index.html
output_html_path = '/Users/catherinetseng/.gemini/antigravity/scratch/index.html'
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Successfully generated index.html at {output_html_path}")
