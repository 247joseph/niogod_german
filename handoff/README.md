# niogod™ rebuild — handoff plan

This folder is the architecture and handoff plan for rebuilding **niogod.de** (canonical, German) and **niogod.com** (English mirror) per the brief dated 2026-05-03. It is not code. It is the document that lets a competent Next.js team start building Monday morning without ambiguity, and that lets you (Joseph) see exactly what is blocked on artifact procurement vs. what can ship now.

> ## Folder consolidation note (read this if you also see `niogod_new` on the desktop)
>
> The legacy site exists in two parallel folders on the desktop today:
> - `~/Desktop/niogod_new/` — English-language legacy site
> - `~/Desktop/niogod_german/` — German-language legacy site (this folder)
>
> **The rebuild collapses both into a single Next.js codebase.** Per the brief §1 and §3.6, niogod.de and niogod.com are served from one deployment with locale-prefix middleware (file 01) — they are not separate projects, and they should not be maintained as separate repos. The two desktop folders are themselves a legacy artifact: a fork that the new architecture eliminates.
>
> The handoff plan in this folder is **identical** to the one in `niogod_new/handoff/` — not a translation, not a divergent variant. One plan, one repo. If you find yourself editing one folder's plan and not the other, the right move is to delete one and reconcile, not to maintain both.
>
> **At cutover** (file 09 Sprint 5 + file 10):
> 1. Both `niogod_new/*.html` and `niogod_german/*.html` are archived to `_legacy_archive/`.
> 2. The new Next.js repo (recommended location: `~/Desktop/niogod-web/` or wherever the team prefers, separate from these two legacy folders) becomes the source of truth.
> 3. Redirects (file 10) handle inbound traffic from both legacy domains/paths.
> 4. The Stuttgart DACH Liaison contact lands in the visible footer; the Bengaluru operational hub is disclosed on the Regional and Compliance Shield pages — both rendered from the *same* component, with locale-aware copy. There is no longer a "German site" and an "English site" — there is one site with two locale faces.

## Read in this order

| # | File | What it gives you |
|---|---|---|
| 00 | `00-reality-check.md` | The honest state of the site given that **no trust artifacts currently exist**. Reframes the launch posture from AÜG to §631 BGB Werkvertrag interim. Read this first — it changes the homepage. |
| 01 | `01-repo-layout.md` | Folder tree for the Next.js 15 App Router monorepo, DE/EN routing convention, file naming. |
| 02 | `02-stack-and-packages.md` | Every package, every version pin, every "why this one" rationale. EU-hosting decision (Vercel Frankfurt vs. Hetzner). |
| 03 | `03-design-tokens.json` + `03-design-tokens.md` | The token JSON file plus the rationale: why cream not white, why Berkeley Mono, why no blue. |
| 04 | `04-component-inventory.md` | Every component the site needs, grouped by primitive / pattern / page-section, in build order. |
| 05 | `05-content-plan.md` | Page-by-page status of copy, where copy is missing, and which artifact each page is blocked on. |
| 06 | `06-mdx-schemas.md` | Frontmatter schema for `/dossiers` (case studies) and `/insights` (long-form) with one worked example each. |
| 07 | `07-trust-artifact-procurement.md` | The critical-path document. Each of the ~25 artifacts in §5 of the brief, who owns it, what it costs, how long it takes, what blocks it. |
| 08 | `08-launch-checklist.md` | The §10 Definition of Done as an actual checklist, with explicit gates and verification commands. |
| 09 | `09-sprint-plan.md` | Sprint 0 (now) → Sprint 1 (foundation) → Sprint 2+ (artifact-gated work) → launch, with realistic dates. |
| 10 | `10-legacy-migration.md` | What to do with the existing `/Desktop/niogod_new/*.html` files: what gets killed, what gets archived, what URLs need 301s. |

## Operating principle

Every page on the new site is shippable when **(a) every claim links to an artifact, or (b) every gap is rendered with an honest amber pending token**. The plan optimizes for honesty as the institutional signal — the brief calls this out at §5.6, and given the current artifact state it is the only ethical posture.

## What is *not* in this plan

- Figma files. The brief asks for Figma + production code; design tokens (file 03) and the component inventory (file 04) are the bridge. Figma comps are a separate deliverable in Sprint 1.
- Legal text. Impressum / Datenschutz / AGB drafting belongs to the German Datenschutzbeauftragter (DSB) and a German Anwalt für IT-Recht. The plan tells the build team where that text plugs in; it does not write it.
- Pricing numbers. §7.5 says ship indicative ranges. The numbers are a commercial decision — file 05 specifies the table format and footnote structure; the actual € figures need your sign-off.
