"""Generate the Mac-style animated icon section (and the rose DM button) for rose-glass.css.

Every icon has an outline and a filled version (like Apple's icon sets). Both are
original 24x24 drawings used as CSS masks, so they take the button's own color.
Hover (or an "on" state) swaps to the filled version and plays a small animation.
"""
import sys
from urllib.parse import quote

L = 'stroke="black" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"'
F = 'fill="black" stroke="black" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
SLASH = '<path stroke="black" stroke-width="1.8" stroke-linecap="round" d="M4 3.5 20 20.5"/>'
# a gap cut around the slash so it stays readable on filled shapes
SLASH_GAP = ('<mask id="g"><rect width="24" height="24" fill="white"/>'
             '<path stroke="black" stroke-width="4.6" stroke-linecap="round" d="M4 3.5 20 20.5"/></mask>')

BUBBLE_FRONT = "M4.5 5h11a1.5 1.5 0 0 1 1.5 1.5v6a1.5 1.5 0 0 1-1.5 1.5H9l-3.5 3v-3h-1A1.5 1.5 0 0 1 3 12.5v-6A1.5 1.5 0 0 1 4.5 5z"
BUBBLE_BACK = "M19.5 9.5h.5A1.5 1.5 0 0 1 21.5 11v5a1.5 1.5 0 0 1-1.5 1.5h-.5V20l-3-2.5H12"
BELL = "M6 16.5v-5a6 6 0 0 1 12 0v5l1.5 2h-15z"
PIN = "M9 3.5h6l-.8 5.2 3.3 3.3v2H6.5v-2l3.3-3.3z"
TRAY = "M3.5 13.5 6 5h12l2.5 8.5V19h-17z"
TRAY_LIP = "M3.5 13.5H8l1.5 2.5h5l1.5-2.5h4.5"
PHONE = "M6.5 3.5h2.2l1.6 4.2-2 1.5a10.5 10.5 0 0 0 6.5 6.5l1.5-2 4.2 1.6v2.2a2 2 0 0 1-2 2A16 16 0 0 1 4.5 5.5a2 2 0 0 1 2-2z"
MIC_STAND = "M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21"
HP_BAND = "M4 15.5v-3.5a8 8 0 0 1 16 0v3.5"
GEAR_TEETH = '<path stroke="black" stroke-width="2.6" d="M12 2.8v3.4M12 17.8v3.4M2.8 12h3.4M17.8 12h3.4M5.5 5.5l2.4 2.4M16.1 16.1l2.4 2.4M5.5 18.5l2.4-2.4M16.1 7.9l2.4-2.4"/>'
QMARK = "M9.6 9.4a2.5 2.5 0 1 1 3.6 2.3c-.7.3-1.2 1-1.2 1.8v.5"

ICONS = {
    "threads":        f'<path {L} d="{BUBBLE_FRONT}"/><path {L} d="{BUBBLE_BACK}"/>',
    "threads-fill":   f'<path {F} d="{BUBBLE_FRONT}"/><path {L} d="{BUBBLE_BACK}"/>',
    "bell":           f'<path {L} d="{BELL}"/><path {L} d="M10 20.5a2 2 0 0 0 4 0"/>',
    "bell-fill":      f'<path {F} d="{BELL}"/><path {L} d="M10 20.5a2 2 0 0 0 4 0"/>',
    "pin":            f'<path {L} d="{PIN}"/><path {L} d="M12 14v6.5"/>',
    "pin-fill":       f'<path {F} d="{PIN}"/><path {L} d="M12 14v6.5"/>',
    "members":        f'<circle {L} cx="9" cy="8" r="3.5"/><path {L} d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path {L} d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18 14.2a6.5 6.5 0 0 1 3.5 5.8"/>',
    "members-fill":   f'<circle {F} cx="9" cy="8" r="3.5"/><path {F} d="M2.5 20a6.5 6.5 0 0 1 13 0z"/><path {L} d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18 14.2a6.5 6.5 0 0 1 3.5 5.8"/>',
    "inbox":          f'<path {L} d="{TRAY}"/><path {L} d="{TRAY_LIP}"/>',
    "inbox-fill":     f'<mask id="m"><rect width="24" height="24" fill="white"/><path stroke="black" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none" d="{TRAY_LIP}"/></mask><path {F} mask="url(#m)" d="{TRAY}"/>',
    "help":           f'<circle {L} cx="12" cy="12" r="9"/><path {L} d="{QMARK}"/><circle cx="12" cy="17" r="1" fill="black"/>',
    "help-fill":      f'<mask id="m"><rect width="24" height="24" fill="white"/><path stroke="black" stroke-width="1.8" stroke-linecap="round" fill="none" d="{QMARK}"/><circle cx="12" cy="17" r="1.1" fill="black"/></mask><circle fill="black" mask="url(#m)" cx="12" cy="12" r="9.8"/>',
    "phone":          f'<path {L} d="{PHONE}"/>',
    "phone-fill":     f'<path {F} d="{PHONE}"/>',
    "video":          f'<rect {L} x="2.5" y="6.5" width="13" height="11" rx="2.5"/><path {L} d="m15.5 10.5 6-3.5v10l-6-3.5"/>',
    "video-fill":     f'<rect {F} x="2.5" y="6.5" width="13" height="11" rx="2.5"/><path {F} d="m15.5 10.5 6-3.5v10l-6-3.5z"/>',
    "profile":        f'<circle {L} cx="12" cy="8.5" r="4"/><path {L} d="M4.5 20.5a7.5 7.5 0 0 1 15 0"/>',
    "profile-fill":   f'<circle {F} cx="12" cy="8.5" r="4"/><path {F} d="M4.5 20.5a7.5 7.5 0 0 1 15 0z"/>',
    "mic":            f'<rect {L} x="9" y="3" width="6" height="11.5" rx="3"/><path {L} d="{MIC_STAND}"/>',
    "mic-fill":       f'<rect {F} x="9" y="3" width="6" height="11.5" rx="3"/><path {L} d="{MIC_STAND}"/>',
    "mic-off":        f'{SLASH_GAP}<g mask="url(#g)"><rect {L} x="9" y="3" width="6" height="11.5" rx="3"/><path {L} d="{MIC_STAND}"/></g>{SLASH}',
    "mic-off-fill":   f'{SLASH_GAP}<g mask="url(#g)"><rect {F} x="9" y="3" width="6" height="11.5" rx="3"/><path {L} d="{MIC_STAND}"/></g>{SLASH}',
    "headphones":     f'<path {L} d="{HP_BAND}"/><rect {L} x="3" y="14" width="4.5" height="7" rx="2"/><rect {L} x="16.5" y="14" width="4.5" height="7" rx="2"/>',
    "headphones-fill": f'<path {L} d="{HP_BAND}"/><rect {F} x="3" y="14" width="4.5" height="7" rx="2"/><rect {F} x="16.5" y="14" width="4.5" height="7" rx="2"/>',
    "headphones-off": f'{SLASH_GAP}<g mask="url(#g)"><path {L} d="{HP_BAND}"/><rect {L} x="3" y="14" width="4.5" height="7" rx="2"/><rect {L} x="16.5" y="14" width="4.5" height="7" rx="2"/></g>{SLASH}',
    "headphones-off-fill": f'{SLASH_GAP}<g mask="url(#g)"><path {L} d="{HP_BAND}"/><rect {F} x="3" y="14" width="4.5" height="7" rx="2"/><rect {F} x="16.5" y="14" width="4.5" height="7" rx="2"/></g>{SLASH}',
    "gear":           f'<circle {L} cx="12" cy="12" r="6"/><circle {L} cx="12" cy="12" r="2.4"/>{GEAR_TEETH}',
    "gear-fill":      f'<path fill="black" fill-rule="evenodd" d="M12 5.2a6.8 6.8 0 1 1 0 13.6 6.8 6.8 0 1 1 0-13.6zM12 9.4a2.6 2.6 0 1 0 0 5.2 2.6 2.6 0 1 0 0-5.2z"/>{GEAR_TEETH}',
}

ROSE = open(sys.argv[2], encoding="utf8").read().strip()


def uri(svg):
    return 'url("data:image/svg+xml,' + quote(svg, safe=" =:/,'.-") + '")'


def icon_uri(body):
    return uri(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">{body}</svg>')


# (icon, button selectors, hover animation, transform-origin)
TARGETS = [
    ("threads", ['[aria-label="Threads" i]'], "tahoe-ic-hop", "50% 50%"),
    ("bell", ['[aria-label^="Notification Settings" i]'], "tahoe-ic-ring", "50% 15%"),
    ("pin", ['[aria-label="Pinned Messages" i]', '[aria-label="Pins" i]'], "tahoe-ic-bob", "50% 90%"),
    ("members", ['[aria-label$="Member List" i]'], "tahoe-ic-hop", "50% 50%"),
    ("inbox", ['[aria-label="Inbox" i]'], "tahoe-ic-dip", "50% 50%"),
    ("help", ['[aria-label="Help" i]'], "tahoe-ic-tilt", "50% 60%"),
    ("phone", ['[aria-label="Start Voice Call" i]'], "tahoe-ic-jiggle", "50% 50%"),
    ("video", ['[aria-label="Start Video Call" i]'], "tahoe-ic-slide", "50% 50%"),
    ("profile", ['[aria-label$="User Profile" i]'], "tahoe-ic-hop", "50% 50%"),
    ("mic", ['[aria-label="Mute" i]'], "tahoe-ic-pop", "50% 50%"),
    ("headphones", ['[aria-label="Deafen" i]'], "tahoe-ic-wobble", "50% 30%"),
    ("gear", ['[aria-label="User Settings" i]'], "tahoe-ic-turn", "50% 50%"),
]
# muted / deafened: these must come after the plain mic/headphones rules
OFF_TARGETS = [
    ("mic-off", ['[aria-label="Unmute" i]', '[aria-label="Mute" i][aria-checked="true"]']),
    ("headphones-off", ['[aria-label="Undeafen" i]', '[aria-label="Deafen" i][aria-checked="true"]']),
]

all_btns = [s for _, sels, _, _ in TARGETS for s in sels] + [s for _, sels in OFF_TARGETS for s in sels]


def join(sels, suffix):
    return ",\n  ".join(f"{s}{suffix}" for s in sels)


out = ["""/* ==========================================================================
   Mac-style animated icons
   Discord's icons on these buttons are hidden and redrawn as outline icons
   that fill in and animate on hover (or while switched on). They use each
   button's own color, so hover states and "muted red" still work.
   Set --tahoe-icons: off in your settings to keep Discord's icons.
   ========================================================================== */
:root {"""]
for name, body in ICONS.items():
    out.append(f"  --tahoe-icon-{name}: {icon_uri(body)};")
out.append(f"  --tahoe-rose: {uri(ROSE)};")
out.append("}\n")

out.append("@container style(--tahoe-icons: on) {")
for name, sels, anim, origin in TARGETS:
    out.append(f"  {join(sels, ' svg')} {{\n    --tahoe-icon: var(--tahoe-icon-{name});\n"
               f"    --tahoe-icon-on: var(--tahoe-icon-{name}-fill);\n    --tahoe-icon-anim: {anim};\n"
               f"    transform-origin: {origin};\n  }}")
for name, sels in OFF_TARGETS:
    out.append(f"  {join(sels, ' svg')} {{\n    --tahoe-icon: var(--tahoe-icon-{name});\n"
               f"    --tahoe-icon-on: var(--tahoe-icon-{name}-fill);\n    --tahoe-icon-anim: tahoe-ic-shake;\n"
               f"    animation: tahoe-ic-shake 0.45s ease-out;\n  }}")

out.append(f"""
  /* draw the icon, hide Discord's */
  {join(all_btns, ' svg')} {{
    background-color: currentColor !important;
    -webkit-mask: var(--tahoe-icon) center / 100% 100% no-repeat;
    mask: var(--tahoe-icon) center / 100% 100% no-repeat;
  }}
  {join(all_btns, ' svg > *')} {{
    opacity: 0 !important;
  }}

  /* hover, or switched on (open panel, member list shown): fill in */
  {join(all_btns, ':hover svg')},
  {join(all_btns, '[aria-expanded="true"] svg')},
  {join(all_btns, '[aria-pressed="true"] svg')} {{
    --tahoe-icon: var(--tahoe-icon-on);
  }}
  /* hover: play the icon's animation */
  {join(all_btns, ':hover svg')} {{
    animation: var(--tahoe-icon-anim) 0.7s ease-in-out;
  }}

  /* the DM / home button: a rose instead of Discord's logo */
  :is([data-list-item-id="guildsnav___home"][class*="childWrapper_"], [data-list-item-id="guildsnav___home"] [class*="childWrapper_"]) {{
    background: var(--tahoe-fill-2) !important;
    transition: background 0.25s;
  }}
  [class*="blobContainer_"][class*="selected_"] :is([data-list-item-id="guildsnav___home"][class*="childWrapper_"], [data-list-item-id="guildsnav___home"] [class*="childWrapper_"]) {{
    background: linear-gradient(150deg, rgba(255, 232, 240, 0.92), rgba(234, 190, 207, 0.82)) !important;
  }}
  :is([data-list-item-id="guildsnav___home"][class*="childWrapper_"], [data-list-item-id="guildsnav___home"] [class*="childWrapper_"]) > svg {{
    width: 34px !important;
    height: 34px !important;
    background: var(--tahoe-rose) center / contain no-repeat !important;
    transform-origin: 50% 90%;
    transition: scale 0.45s var(--tahoe-bounce);
  }}
  :is([data-list-item-id="guildsnav___home"][class*="childWrapper_"], [data-list-item-id="guildsnav___home"] [class*="childWrapper_"]) > svg > * {{
    opacity: 0 !important;
  }}
  [class*="blobContainer_"]:hover :is([data-list-item-id="guildsnav___home"][class*="childWrapper_"], [data-list-item-id="guildsnav___home"] [class*="childWrapper_"]) > svg {{
    scale: 1.08;
    animation: tahoe-ic-sway 0.9s ease-in-out;
  }}
}}

@keyframes tahoe-ic-ring {{ 0%, 100% {{ rotate: 0deg; }} 15% {{ rotate: 16deg; }} 30% {{ rotate: -13deg; }} 45% {{ rotate: 9deg; }} 60% {{ rotate: -6deg; }} 75% {{ rotate: 3deg; }} }}
@keyframes tahoe-ic-turn {{ from {{ rotate: 0deg; }} to {{ rotate: 90deg; }} }}
@keyframes tahoe-ic-pop {{ 0%, 100% {{ scale: 1; }} 35% {{ scale: 1.2; }} 65% {{ scale: 0.94; }} }}
@keyframes tahoe-ic-hop {{ 0%, 100% {{ translate: 0 0; }} 35% {{ translate: 0 -3px; }} 65% {{ translate: 0 0.5px; }} }}
@keyframes tahoe-ic-jiggle {{ 0%, 100% {{ rotate: 0deg; }} 20% {{ rotate: -14deg; }} 40% {{ rotate: 12deg; }} 60% {{ rotate: -8deg; }} 80% {{ rotate: 4deg; }} }}
@keyframes tahoe-ic-bob {{ 0%, 100% {{ translate: 0 0; rotate: 0deg; }} 40% {{ translate: 0 -3px; rotate: -10deg; }} 70% {{ translate: 0 0.5px; rotate: 3deg; }} }}
@keyframes tahoe-ic-dip {{ 0%, 100% {{ translate: 0 0; }} 40% {{ translate: 0 2.5px; }} 70% {{ translate: 0 -0.5px; }} }}
@keyframes tahoe-ic-tilt {{ 0%, 100% {{ rotate: 0deg; }} 40% {{ rotate: -16deg; }} 70% {{ rotate: 5deg; }} }}
@keyframes tahoe-ic-slide {{ 0%, 100% {{ translate: 0 0; }} 40% {{ translate: 3px 0; }} 70% {{ translate: -0.5px 0; }} }}
@keyframes tahoe-ic-wobble {{ 0%, 100% {{ rotate: 0deg; }} 25% {{ rotate: -10deg; }} 50% {{ rotate: 8deg; }} 75% {{ rotate: -4deg; }} }}
@keyframes tahoe-ic-shake {{ 0%, 100% {{ translate: 0 0; }} 20% {{ translate: -2px 0; }} 40% {{ translate: 2px 0; }} 60% {{ translate: -1.5px 0; }} 80% {{ translate: 1px 0; }} }}
@keyframes tahoe-ic-sway {{ 0%, 100% {{ rotate: 0deg; }} 30% {{ rotate: -9deg; }} 60% {{ rotate: 6deg; }} 85% {{ rotate: -2deg; }} }}
""")

open(sys.argv[1], "w", encoding="utf8").write("\n".join(out))
print("icons:", len(ICONS), "buttons:", len(all_btns))
