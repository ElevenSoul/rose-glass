# macOS Tahoe Theme for Discord (Vencord) — Design

## Intent
Make Discord on Windows look and feel like a native app on current macOS (Tahoe, "Liquid Glass"), as a full restyle rather than a recolor.

## Goals
- Frosted-glass panels (server list, channel list, member list, chat, popups) over a wallpaper drawn inside Discord.
- Mac-style red/yellow/green window buttons on the left of Discord's title bar, replacing the Windows minimize/maximize/close.
- Tahoe shapes: large rounded corners, floating inset panels, pill-shaped controls, thin overlay scrollbars, soft shadows.
- macOS blue accent, Mac-style menus, context menus, tooltips, modals and switches.
- Follows Discord's own light/dark setting, so both modes are supported.
- Settings at the top of the file: wallpaper image, glass strength (including "off"), accent color, corner radius.

## Non-goals
- Real transparency to the Windows desktop (option B). Not doing it.
- Changing Discord's behavior or adding features. This is CSS only, with no plugins.
- Restyling every niche screen perfectly in v1 (for example the deep settings subpages or the activity/game launcher). They should stay usable, with lighter polish.

## Anti-goals (failure even if it "works")
- Text that's hard to read over the glass.
- Laggy scrolling from heavy blur.
- Using Apple's copyrighted wallpapers or icons.

## Constraints
- Vencord on Discord desktop (Windows). Installed at `%APPDATA%\Vencord\themes`.
- Discord class names are hashed and change between updates. To keep it stable, target the `[class*="name_"]` substrings and Discord's CSS variables, not full hashed names.
- The SF Pro font isn't on Windows. Font stack: `SF Pro Display/Text` (used if installed), then **Inter** (loaded from Google Fonts), then the system UI font.
- Blur only applies to content inside the Discord window.

## Approaches considered
- **A. Built-in wallpaper with frosted glass (chosen).** Looks closest to Tahoe, stays readable and works without changing settings. Trade-off: the glass shows the wallpaper, not your real desktop.
- B. Real see-through window. Windows can't blur what's behind the window, so it ends up clear rather than frosted, has readability problems and needs a settings change plus a restart.
- C. Solid panels. Most readable and lightest, but loses the glass that makes Tahoe look like Tahoe.

## Design
- **One file:** `macOS-Tahoe.theme.css`, with a Vencord metadata header. The source lives in `ElevenTheme/` and a copy goes into the Vencord themes folder.
- **Settings block (`:root` variables):** `--tahoe-wallpaper`, `--tahoe-glass-blur`, `--tahoe-glass-opacity`, `--tahoe-accent`, `--tahoe-radius`.
- **Wallpaper:** an original layered-gradient "lake at dusk" wallpaper made in CSS, with separate light and dark versions. You can replace it with your own image `url()`.
- **Glass:** semi-opaque tinted fill + `backdrop-filter: blur() saturate()` + a 1px light inner edge highlight + a soft shadow.
- **Layout (revised after the first preview felt "Android"):** the server list, channel list and user panel share one floating glass sidebar, like Finder or Mail. The chat sits directly on the tinted window. The member list is a matching floating glass panel on the right. Selection uses a soft gray highlight with an accent-colored icon, not a solid accent fill. Text is smaller and tighter.
- **Motion:** spring curves (CSS `linear()`) on menus, popouts, tooltips, dialogs, channel selection, server icons, reactions and newly arrived messages. Respects reduced motion (the OS setting and Discord's own).
- **Theme mapping:** override Discord's background, text and interactive variables under `.theme-dark` / `.theme-light` so that unstyled screens still inherit the look.
- **Title bar:** the Windows buttons become 12px traffic-light circles on the left, and their glyphs show on hover.
- **Order of sections:** settings, then fonts, then color variables, then wallpaper and layout panels, then the title bar, then the server list, then channels, then chat and composer, then the member list, then popouts/menus/tooltips/modals, then controls (buttons, switches, inputs), then scrollbars.

## Left to the builder
- Exact color values and blur amounts, tuned for readability.
- Which selectors to use for each area, checked against the current Discord build.
