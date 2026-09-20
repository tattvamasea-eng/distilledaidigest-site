# D.A.D Issue #34 research pack
Coverage: Saturday 6 September – Saturday 12 September 2026
Live site latest: Issue #33 (https://distilledaidigest.com/issues/issue-33.html), week Aug 30–Sep 5.
Do not re-feature #33 mains: GPT-6 Astra; Zendesk outcome pricing; AIUC-1 / KPMG aIQ; AWS SI/BVR pricing; Snowflake Cortex AI Gateway.
McKinsey State of AI 2026 was already on the #33 pick list — do not re-offer.
Gmail scan 2026-09-12: no usable research leads (consumer newsletters, Luma, Groupon).
Aham delegate_task timed out; research completed in-session from primary pages and wire coverage.

---

## 1. OpenAI publishes a Navier–Stokes Millennium Prize solution
- Date: 8 Sep 2026 (update 10 Sep on concurrent-work / user-input investigation)
- Primary: https://openai.com/index/navier-stokes-solution/
- Facts: Internal system “significantly more capable than GPT-6 Astra” produced an analytical proof plus Lean formalization that 3D incompressible Navier–Stokes can develop a finite-time singularity from smooth initial data (Clay statements C and D). Vortex that spirals inward and elongates; energy remains finite; smooth external force. OpenAI will not claim the Clay prize. Training of the internal model ongoing since 28 Aug.
- Enterprise angle: The capability jump is not in the ChatGPT SKU you can buy this week. Boards that treated Astra as the ceiling need a “what sits behind the API” question for science, simulation, and digital-twin roadmaps. Also a disclosure/ stewards question: a lab just demonstrated a result it will not submit for the prize.
- Data: Clay problem open ~90 years; internal model > Astra; Lean formalization released.

## 2. NSA / CISA / FBI AA26-251A: industrial-scale distillation
- Date: 8 Sep 2026
- Primary: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a
- Facts: Joint advisory names DeepSeek, Moonshot AI, Alibaba, MiniMax, StepFun, Z.AI. Billions of tokens / millions of exchanges from Claude, GPT, Gemini, and Grok variants since at least late 2024, “likely with Chinese government awareness.” Distillation described as the core of their development strategy, not a supplement. TTPs: native APIs, cloud, aggregators, “transfer stations.” Three actions: detect anomalous usage (subscription-to-usage, new accounts at max quota); alter responses to suspected distillation; share intel across providers/clouds/aggregators.
- Enterprise angle: If you buy DeepSeek / Qwen / Kimi / MiniMax into production, this is now a named national-security advisory, not a TOS footnote. If you sell or proxy frontier APIs, you are in the detection perimeter. Procurement and legal need a written position this quarter.
- Data: six named firms; late 2024 start; three mandated action classes.

## 3. Qualcomm × Amazon multi-generation custom AI chips
- Date: 8 Sep 2026
- Primary: https://www.qualcomm.com/news/releases/2026/09/qualcomm-announces-multi-generational-product-collaboration-with
- Wire: Reuters / Bloomberg — Amazon right to acquire as much as ~$4B in Qualcomm stock; custom silicon for AWS AI infrastructure; optical interconnects toward 1.6T.
- Enterprise angle: AWS inference supply is no longer “Nvidia or Trainium.” Custom Qualcomm silicon + optics is a multi-year lock-in and a second-source story for CIOs who have been single-threaded on GB200 allocations.
- Data: multi-gen; ~$4B equity right; 1.6T optics target.

## 4. Google €13 billion Finland AI infrastructure (largest single European bet)
- Date: 9 Sep 2026
- Primary: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-ai-commitment-to-finland/
- Facts: At least €13B over 2027–2028 in digital infrastructure, clean energy, partnerships. 22-year agreement supporting Loviisa nuclear life extension (DW/BBC: up to half the plant’s output). 94 MW battery. Construction 2027–28: >37,000 jobs nationwide, €3.6B annual GDP contribution. €31M into Hamina, Kajaani, Muhos, Vaala over four years; AI upskilling for >4,400 workers.
- Enterprise angle: Sovereign-EU and Nordic capacity is being bought with nuclear PPAs, not press releases. Ask cloud vendors for energization dates and power mix, not GPU reservation letters. Continues the #33 Texas “ghost demand” thread without repeating it.
- Data: €13B / 2 years; 22-year nuclear; 94 MW battery; 37,000 construction jobs.

## 5. Oracle Q1 FY27: $664B RPO, AI cloud still supply-constrained
- Date: 10 Sep 2026
- Primary: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx
- Facts: Total rev $19.3B +30%. Cloud $11.6B +62%. IaaS $7.4B +121%. RPO $664B, +$209B y/y. >$30B additional AI cloud contracts in the quarter. 850 MW additional datacenter capacity delivered. >300,000 GPUs delivered since end of Q4 (almost 3× Q4). OCF $23B +184%. FCF −$5B. Capex ~$28.5B. FY27 total rev guided at least $90B.
- Enterprise angle: The constraint is still delivery, not demand. Multi-cloud AI deals that assume Oracle capacity in FY27 need GPU and MW dates in the contract, plus a walk-away if RPO conversion slips. Customer prepayments are now part of how this build is financed.
- Data: $664B RPO; $30B+ AI bookings; 850 MW; 300k GPUs; FCF −$5B.

## 6. Microsoft plans ~38 GW of data-center capacity by 2032
- Date: 10 Sep 2026
- Source: Bloomberg feature (people familiar); Reuters recap. Not a Microsoft IR primary.
- Facts: ~12 GW now → >38 GW in 2032. Only ~2 GW of current capacity is AI-chip-centric; that share expected toward about one-third of the 38 GW. Label as reported plan, not a filed capex guide.
- Enterprise angle: Azure availability and price will track interconnect and power, not model SKUs. Pair with #33 Texas queue: the CIO question is which of your workloads are actually reserved against energized MW.
- Data: 12 → 38 GW; ~2 GW AI-specific today.

## 7. DeepSeek V4.1 Flash GA; V4-Pro traffic reroutes 14 Sep
- Date: 10 Sep 2026 (reroute 14 Sep 12:00 Beijing / 04:00 UTC)
- Sources: DeepSeek API docs + contemporaneous coverage (Datastudios, Apidog, 36Kr). Treat vendor benches as vendor benches.
- Facts: New MoE architecture; coverage cites ~552B total / 8B active prefill / 16B decode; native vision. V4-Pro requests to be served by V4.1 Flash at Flash prices from 14 Sep until a future V4.1 Pro. Material token-price cut vs prior Pro.
- Enterprise angle: Same week as AA26-251A. Cost and national-security screens now move together. Anyone with DeepSeek in production has a model-id and ToS review before 14 Sep, and a board question about whether the savings survive a US advisory.
- Data: GA 10 Sep; Pro alias dies 14 Sep; Flash economics replace Pro.

## 8. OpenAI GPT-Live-1 in the API; Yelp Host / Hatch day-one
- Date: 10 Sep 2026
- Primary: https://openai.com/index/introducing-gpt-live-1-in-the-api/
- Yelp: https://blog.yelp.com/news/yelp-host-and-hatch-gpt-live-1/
- Facts: Full-duplex voice model in the API for apps and business workflows. Yelp putting it as the front-end voice layer on Yelp Host (restaurants; >1M calls since Oct 2025 per secondary recap) and Hatch. Do not quote $0.05/min unless confirmed on the OpenAI page.
- Enterprise angle: Contact-center and local-services voice is leaving the “bot that holds for a human” demo. The buy is voice layer + business context + write-back, not a model bake-off. Ask for interruption handling, recording/retention, and who owns the transcript.
- Data: API GA 10 Sep; Yelp named design partner.

## 9. Pentagon in talks to lend ~$5B to Fluidstack (WSJ)
- Date: 10 Sep 2026
- Source: WSJ via Reuters. Talks, not a closed deal. Office of Strategic Capital. Use is US manufacturing capacity for data-center components (power, cooling), not a new AI hall.
- Enterprise angle: Defense is moving from AI customer to AI-infrastructure lender. Neocloud counterparty risk now includes a possible sovereign credit overlay. Treat as watch-item until OSC confirms.
- Data: ~$5B talks; OSC; components not a campus.

## 10. Anthropic IPO timetable slips; $15B revolver in view
- Date: wires 5–6 Sep 2026 (still the lab-finance story of this week; #33 did not run it)
- Sources: Reuters / Bloomberg recaps. Company has not confirmed a listing date.
- Facts as reported: S-1 later in September; marketing as early as mid-October; revolving credit facility sized around $15B (up from a prior ~$10B target / vs ~$2.5B last year). Banks: Morgan Stanley lead-left; Goldman, JPM in the group. Valuation “up to $2T” is investor talk, not a filing. CNBC Aug 17 ARR ~$65B in July is unsourced to Anthropic itself — do not treat as audited.
- Enterprise angle: Counterparty and concentration risk on the second frontier lab. Procurement should ask where Claude capacity sits if a public-company cycle starts in October, and whether Enterprise Frontier Safeguards / ZDR terms change under IPO counsel.
- Data: $15B facility (reported); mid-October marketing (reported); no company listing date.

## Consulting / analyst (this week)
- McKinsey State of AI 2026: already offered on #33 pick list (40% of >$1B firms scaling agents; 37% EBIT contribution unchanged; ~6% high performers). Do not re-offer as a main.
- Gartner 2026 Hype Cycle for Agentic AI: evergreen page, no confirmed this-week drop found. Usable as CIO Corner color, not a story.
- Forrester / Deloitte / KPMG: no fresh in-window flagship comparable to AA26-251A or Oracle IR.

## Out of window / do not use as mains
- Google Gemini Enterprise flexible billing: Cloud blog 26 Aug 2026.
- TravelersLLM: CIO Dive 24 Aug / company 30 Jun.
- Carnegie Mellon / Larridin 10-K study: report 12 Aug, CFO Dive 17 Aug.
- Nvidia–Hugging Face $12.93B: was on #33 candidate list; do not recycle.
- GPT-6 Astra / Fable 5.1 / Mythos 5.1 / Gemini 3.8 Flash: #33.
