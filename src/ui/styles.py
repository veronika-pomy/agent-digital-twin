"""Styling constants for the digital twin Gradio app."""

GOLD = "#f5d98b"
BLUE = "#102a5f"
PURPLE = "#a984ff"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
:root {
  --twin-gold: #f5d98b;
  --twin-blue: #102a5f;
  --twin-purple: #a984ff;
  --twin-cyan: #74d7ff;
  --twin-amethyst: #d8c6ff;
  --twin-bg: #070910;
  --twin-bg-2: #12182c;
  --twin-surface: rgba(247, 247, 255, 0.10);
  --twin-surface-2: rgba(255, 255, 255, 0.15);
  --twin-surface-3: rgba(11, 14, 27, 0.48);
  --twin-border: rgba(230, 232, 255, 0.20);
  --twin-border-strong: rgba(230, 232, 255, 0.34);
  --twin-text: #f5f5fa;
  --twin-muted: #a8adbc;
  --twin-shadow: rgba(0, 0, 0, 0.36);
  --twin-glow: rgba(169, 132, 255, 0.32);
  --twin-radius: 28px;
  --twin-radius-small: 18px;
}

/* Light mode: Gradio adds `.dark` to <body> when dark; absence = light.
   Only the neutral palette flips; accents stay in the same family. */
body:not(.dark) {
  --twin-bg: #eff1f8;
  --twin-bg-2: #dce3f5;
  --twin-surface: rgba(255, 255, 255, 0.62);
  --twin-surface-2: rgba(255, 255, 255, 0.78);
  --twin-surface-3: rgba(246, 247, 253, 0.72);
  --twin-border: rgba(88, 97, 130, 0.18);
  --twin-border-strong: rgba(88, 97, 130, 0.28);
  --twin-text: #171923;
  --twin-muted: #667085;
  --twin-shadow: rgba(56, 64, 90, 0.18);
  --twin-glow: rgba(169, 132, 255, 0.22);
  --twin-cyan: #2f79c7;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app {
  background:
    radial-gradient(circle at 16% 8%, rgba(216, 198, 255, 0.26), transparent 30%),
    radial-gradient(circle at 84% 4%, rgba(44, 92, 180, 0.36), transparent 34%),
    linear-gradient(145deg, var(--twin-bg), var(--twin-bg-2) 58%, var(--twin-bg)) !important;
  background-attachment: fixed !important;
}

/* ---------- Stable layout ---------- */
.gradio-container {
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 880px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 32px 24px 48px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 28px !important;
  font-weight: 650 !important;
  letter-spacing: 0 !important;
  border-left: 0;
  padding-left: 0 !important;
  margin: 4px 0 8px !important;
  text-align: left !important;
  text-shadow: 0 1px 22px rgba(216, 198, 255, 0.24);
}
.gradio-container h1::after {
  content: "";
  display: block;
  width: 128px;
  height: 4px;
  margin-top: 14px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--twin-purple), var(--twin-cyan), rgba(245, 217, 139, 0.55));
  box-shadow:
    0 0 18px rgba(169, 132, 255, 0.36),
    0 0 28px rgba(116, 215, 255, 0.20);
}
.gradio-container .prose,
.gradio-container p {
  color: var(--twin-muted) !important;
}

/* ---------- Liquid glass radius ---------- */
.chatbot, .chatbot *, .block, .form,
button, input, textarea,
.examples button {
  border-radius: var(--twin-radius-small) !important;
}

/* ---------- Block surfaces ---------- */
.block, .form { background: transparent !important; box-shadow: none !important; }

/* ---------- Hide the Chatbot label / header strip ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ---------- Chatbot frame ---------- */
.chatbot, .chatbot.block {
  position: relative !important;
  overflow: hidden !important;
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.06)),
    var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  min-height: 460px !important;
  border-radius: var(--twin-radius) !important;
  box-shadow:
    0 28px 80px var(--twin-shadow),
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(255, 255, 255, 0.08) !important;
  backdrop-filter: blur(28px) saturate(1.45) !important;
  -webkit-backdrop-filter: blur(28px) saturate(1.45) !important;
}
.chatbot::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    linear-gradient(115deg, rgba(255, 255, 255, 0.32), transparent 18%, transparent 76%, rgba(255, 255, 255, 0.12)),
    radial-gradient(circle at 18% 12%, rgba(245, 217, 139, 0.16), transparent 22%),
    radial-gradient(circle at 76% 18%, rgba(169, 132, 255, 0.22), transparent 24%);
  opacity: 0.72;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* ---------- Reset borders on every bubble variant first ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 1px solid rgba(255, 255, 255, 0.14) !important;
  box-shadow:
    0 10px 28px rgba(0, 0, 0, 0.18),
    inset 0 1px 0 rgba(255, 255, 255, 0.18) !important;
  padding: 5px 12px !important;
  border-radius: 16px !important;
  backdrop-filter: blur(18px) saturate(1.35) !important;
  -webkit-backdrop-filter: blur(18px) saturate(1.35) !important;
}

/* ---------- Bubble backgrounds (broad to cover Gradio variants) ---------- */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background:
    linear-gradient(145deg, rgba(98, 145, 224, 0.88), rgba(72, 111, 190, 0.78)) !important;
  color: #ffffff !important;
  border-color: rgba(214, 225, 255, 0.42) !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.18), rgba(216, 198, 255, 0.10)),
    var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  border-color: var(--twin-border-strong) !important;
}

/* ---------- Assistant glint ----------
   Apply to every common bubble class for assistant rows, then suppress on any
   nested instance so the glow lands on the outermost matching element only. */
.message-row.bot-row .message,
.message-row.bot-row .bubble,
.message-row.bot-row .message-bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .bubble,
.message-row[data-role="assistant"] .message-bubble {
  border-left: 1px solid rgba(216, 198, 255, 0.52) !important;
  box-shadow:
    0 12px 30px rgba(15, 18, 32, 0.20),
    -8px 0 24px rgba(169, 132, 255, 0.13),
    inset 0 1px 0 rgba(255, 255, 255, 0.22) !important;
}

.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,
.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,
.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border-left: 0 !important;
}

/* ---------- Uniform font size in bubbles ----------
   The "first paragraph different size" was caused by a leaky `.prose p:first-of-type`
   selector. Force every paragraph in a bubble to the same size. */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14px !important;
  line-height: 1.28 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;
  line-height: 1.28 !important;
  margin: 0 0 4px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Strip stray internal borders/backgrounds from anything inside a bubble */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: underline;
}

/* ---------- Input row alignment ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; }

textarea, input[type="text"] {
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.14), rgba(255, 255, 255, 0.06)),
    var(--twin-surface-3) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14px !important;
  padding: 12px 14px !important;
  line-height: 1.4 !important;
  min-height: 48px !important;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.14) !important;
  backdrop-filter: blur(22px) saturate(1.35) !important;
  -webkit-backdrop-filter: blur(22px) saturate(1.35) !important;
}
textarea:focus, input[type="text"]:focus {
  border-color: rgba(216, 198, 255, 0.68) !important;
  outline: none !important;
  box-shadow:
    0 0 0 1px rgba(216, 198, 255, 0.35),
    0 0 30px rgba(169, 132, 255, 0.22),
    inset 0 1px 0 rgba(255, 255, 255, 0.18) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  border: 1px solid var(--twin-border) !important;
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.06)),
    var(--twin-surface) !important;
  color: var(--twin-text) !important;
  padding: 0 16px !important;
  min-height: 48px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.18) !important;
  backdrop-filter: blur(18px) saturate(1.35) !important;
  -webkit-backdrop-filter: blur(18px) saturate(1.35) !important;
  transition: background 0.16s ease, color 0.16s ease, border-color 0.16s ease, transform 0.16s ease;
}
button:hover {
  border-color: rgba(216, 198, 255, 0.64) !important;
  color: var(--twin-amethyst) !important;
  transform: translateY(-1px);
}

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background:
    linear-gradient(145deg, rgba(245, 217, 139, 0.96), rgba(169, 132, 255, 0.84)) !important;
  border: 1px solid rgba(255, 247, 222, 0.56) !important;
  color: #11131d !important;
  min-height: 48px !important;
  align-self: stretch !important;
  padding: 0 14px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background:
    linear-gradient(145deg, #fff1ba, #cbb5ff) !important;
  border-color: rgba(255, 255, 255, 0.74) !important;
  color: #11131d !important;
}

/* ---------- Submit-button icon: center vertically and size correctly ---------- */
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #11131d !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Examples ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 12px !important;
  margin-top: 20px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples tbody,
.examples tr,
[data-testid="examples"] {
  display: grid !important;
  gap: 10px !important;
}
.examples td {
  padding: 0 !important;
}
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.14), rgba(255, 255, 255, 0.05)),
    var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  padding: 10px 14px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: rgba(245, 217, 139, 0.42) !important;
  color: var(--twin-text) !important;
  background:
    linear-gradient(145deg, rgba(245, 217, 139, 0.14), rgba(216, 198, 255, 0.08)),
    var(--twin-surface) !important;
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 4px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover { color: var(--twin-gold) !important; }

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, var(--twin-amethyst), var(--twin-blue));
  border-radius: 999px;
}
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); }

/* ---------- Selection ---------- */
::selection { background: var(--twin-amethyst); color: #11131d; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 22px 14px 36px !important; }
  .gradio-container h1 { font-size: 22px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
