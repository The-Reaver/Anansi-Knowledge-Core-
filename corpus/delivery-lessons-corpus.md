# Delivery Lessons Corpus: Real Postmortems

Every item below is drawn from a real, publicly documented incident. Sources are linked and
dated. Where a quote is marked, it is pulled from the cited page; unmarked text is a summary
in the corpus author's own words. Where a category had no strong real match after a genuine
search, that is stated directly instead of padded with a weak or constructed substitute.

Field format and the ability taxonomy (VER, ART, REL, REV, RAT, RCK, REC, FAI) are defined in
`taxonomy-and-format.md`.

**Sourcing note (this pass):** the ART items below were researched in a session where direct
page-fetching was blocked by network policy for effectively every general-web domain except
`raw.githubusercontent.com`. Facts were cross-checked across multiple independent search
results before inclusion, but no text on the page was independently re-fetched and confirmed
verbatim, so none of the ART items below carry quoted material — Situation text is paraphrase
only. Anyone using these items in something quote-sensitive should verify against the source
URL directly before quoting it.

---

## VER — Verification

### VER-001: CrowdStrike Content Validator let a broken update pass
**Situation:** On July 19, 2024, CrowdStrike shipped a Falcon sensor configuration update containing a bug in its IPC Template Type. The company's Content Validator, the layer meant to check updates before release, had a bug that let the faulty configuration through. CrowdStrike later stated that "due to baseline trust from the previous tests and successful deployments, no additional testing like dynamic checks was performed," and the update was never run on real developer machines before shipping.
**Impact:** Roughly 8.5 million Windows systems crashed worldwide from an out-of-bounds memory read once the Content Interpreter processed the bad config.
**Lesson:** A validator that checks structure isn't the same as verification against the real running system. When "tests passed" starts meaning "the validator didn't object" instead of "we ran it," that gap has to be closed before every release, not just the first one.
**Source:** [CrowdStrike: 'Content Validator' bug let faulty update pass checks](https://www.bleepingcomputer.com/news/security/crowdstrike-content-validator-bug-let-faulty-update-pass-checks/), July 2024.
**Cost:** L

### VER-002: Cloudflare deployed an untested WAF rule globally
**Situation:** On July 2, 2019, Cloudflare rolled out new Web Application Firewall rules meant to run in simulated (non-blocking) mode. One rule's regular expression caused catastrophic backtracking, spiking CPU to 100% on every edge machine at once. Cloudflare's own writeup states plainly: "these WAF rules were deployed globally in one go," and that their "testing processes were insufficient in this case."
**Impact:** Global traffic dropped 82% at the worst point; the incident ran about 110 minutes from detection to full restoration.
**Lesson:** A rule or config change with global reach needs a staged rollout and a real load test before every machine gets it at once, not just before the first deploy of the feature.
**Source:** [Cloudflare: Cloudflare outage on July 2, 2019](https://blog.cloudflare.com/cloudflare-outage/), July 2019.
**Cost:** L

### VER-003: Facebook's own audit tool had the exact bug it existed to prevent
**Situation:** On October 4, 2021, a routine maintenance command intended to assess available backbone capacity was run against Facebook's global backbone network. Facebook's systems include an audit tool specifically built to catch and stop commands like this one before they cause outsized damage, but a bug in that audit tool let the command through anyway, and it ended up withdrawing the BGP advertisements for Facebook's own DNS servers from the backbone. Because those DNS servers became unreachable, and the same backbone loss also broke the remote tools engineers would normally use to fix it, engineers had to be dispatched physically to data centers to restore access.
**Impact:** ~6 hours of complete outage across Facebook, Instagram, WhatsApp, and Oculus, plus Meta's internal tools, globally.
**Lesson:** A safety check that exists specifically to catch one class of dangerous command is a single point of failure for that entire class — if the checker has its own bug, "we have an audit tool for this" provides zero actual protection. Verify the audit tool's negative case (that it actually blocks the bad command) as rigorously as the command itself; a check nobody has watched actually fail a bad input is unverified.
**Source:** [Meta Engineering: More details about the October 4 outage](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/), October 5, 2021.
**Cost:** L

### VER-004: AppNexus's staging environment couldn't trigger the bug that took down production
**Situation:** On September 17, 2013, AppNexus pushed a routine data update to its "impbus" ad-serving clusters after the update had already passed both staging and production validation tests. The update triggered a double-free bug, but the bug only manifested after a specific time delay had elapsed in the running process — a condition staging never exercised, since nothing in the validation process held the update under running load for that long before marking it passed. Once the update reached roughly 900 production impbus servers worldwide, they crashed within moments of each other as the same delay elapsed on each one nearly simultaneously.
**Impact:** Ad serving stopped entirely, then ran in a partially degraded state, for roughly two and a half hours total.
**Lesson:** "Passed staging" only verifies against the conditions staging actually reproduces. If a bug's trigger depends on elapsed time, sustained load, or any other property a short validation run doesn't hold long enough to hit, staging will pass and production will still fail — match staging's duration and conditions to what production actually does, not just its inputs.
**Source:** [Xandr Engineering: 2013–09–17 Outage Postmortem](https://medium.com/xandr-tech/2013-09-17-outage-postmortem-586b19ae4307), September 2013.
**Cost:** M

---

## ART — Artifact Creation

### ART-001: The FBI's Virtual Case File was never actually delivered
**Situation:** Starting in 2000, the FBI contracted SAIC to build the Virtual Case File, a system meant to let agents search and share case data digitally instead of on paper, as part of the larger Trilogy IT modernization program. Requirements changed continuously through development and the FBI itself lacked the technical staff to manage the build, and after roughly $170 million had been spent, the agency abandoned the project in April 2005 without ever deploying it. An independent assessment by the Aerospace Corporation, commissioned once problems became undeniable, found the delivered software incomplete and so poorly built it would not have been usable under real field conditions even if finished.
**Impact:** ~$170 million spent over five years with zero working software delivered to agents; the FBI restarted case-management modernization from scratch under a new program (Sentinel).
**Lesson:** Years of "on track" status reports mean nothing if no one has run the actual end-to-end system. Gate continued funding on a working, integration-tested build at fixed checkpoints — not on requirements documents, schedule confidence, or vendor status updates.
**Source:** [IEEE Spectrum: Who Killed the Virtual Case File?](https://spectrum.ieee.org/who-killed-the-virtual-case-file), September 2005; background also at [Wikipedia: Virtual Case File](https://en.wikipedia.org/wiki/Virtual_Case_File).
**Cost:** L

### ART-002: Denver International Airport's automated baggage system never worked at scale
**Situation:** Denver International Airport was designed around a fully automated baggage-routing system — miles of track and thousands of destination-coded carts controlled by a central system — intended to route bags airport-wide without manual sorting. The system could not reliably load, route, or unload bags without jamming, misrouting, or destroying them once tested at anything close to real volume, and a 1994 GAO review documented the resulting schedule slip. The airport's opening was pushed back about 16 months at roughly $1 million per day in carrying costs, and it eventually opened in February 1995 using a conventional manual system for most airlines, with the automated system limited to a fraction of its intended scope.
**Impact:** ~16-month delay, hundreds of millions of dollars in added cost; United Airlines, the system's largest user, formally abandoned it entirely in August 2005 after roughly a decade of parallel manual backup.
**Lesson:** A system this complex should never be load-bearing for a fixed go-live date (the airport opening) until it has been proven, end-to-end, at real production volume — not vendor-demo volume. If there's no honest way to say "not ready" without it being a crisis, the fallback plan isn't real.
**Source:** [GAO: New Denver Airport — Impact of the Delayed Baggage System (GAO/RCED-95-35BR)](https://www.govinfo.gov/content/pkg/GAOREPORTS-RCED-95-35BR/html/GAOREPORTS-RCED-95-35BR.htm), October 1994.
**Cost:** L

### ART-003: London Ambulance Service's dispatch system collapsed within days of launch
**Situation:** On October 26, 1992, the London Ambulance Service switched its entire dispatch operation over to a newly built Computer Aided Dispatch (CAD) system without first proving it under real peak call volume. Within days the system was assigning multiple ambulances to the same incident, losing track of others, and falling further behind as its own backlog compounded; by November 4, 1992 it stopped printing dispatch details altogether and LAS reverted to a fully manual, paper-and-radio process. A public inquiry followed and the chief executive resigned.
**Impact:** Days of severely degraded ambulance dispatch across London, including anecdotal reports of waits of several hours for some calls, before full reversion to manual operation; the case is now a standard citation in software engineering failure literature.
**Lesson:** Cutting over to a new system on the same day you retire the fallback, without first proving the new system at true peak load, turns any rollout bug into an outage with no way back. Run the new and old systems in parallel until the new one has demonstrably handled real peak volume, not just average load.
**Source:** [Wikipedia: LASCAD](https://en.wikipedia.org/wiki/LASCAD); public inquiry report ("the Page Report"), 1993.
**Cost:** L

---

## REL — Release

### REL-001: Knight Capital's deployment tool reported success on a partial rollout
**Situation:** In 2012, an engineer at Knight Capital reused a bit flag that had been tied to old, deprecated order-routing logic (nicknamed "Power Peg") since 2003. That dead code was never removed from the server image. When the new code shipped to Knight's eight SMARS trading servers, one machine was down for maintenance and rejected the deployment. The deployment script "would fail silently, continue to update the other machines, and report success," so nobody knew one server was still running the old logic.
**Impact:** The stale server started executing millions of erroneous trades against the live market. Knight lost roughly $440 million in 45 minutes before trading was halted.
**Lesson:** A deployment tool that reports success without confirming every target actually received and is running the new artifact will eventually ship a release that's half-old and half-new, and nothing downstream will know to check.
**Source:** [The Knight Capital Disaster](https://specbranch.com/posts/knight-capital/), Speculative Branches; also documented in the SEC's 2013 order against Knight Capital.
**Cost:** L

### REL-002: A mistyped AWS command removed more capacity than intended
**Situation:** On February 28, 2017, an AWS S3 engineer ran a command meant to remove a small number of servers from a billing subsystem for routine debugging. One input to the command was entered incorrectly, and a much larger set of servers was removed, including servers that supported the index and placement subsystems underlying all of S3. Both had to restart from scratch. AWS's own summary states the tool was later changed "to remove capacity more slowly" with "safeguards to prevent capacity from being removed when it will take any subsystem below its minimum required capacity level," meaning no such floor existed at the time.
**Impact:** A roughly four-hour S3 outage that cascaded into EC2, EBS, and Lambda across the US-EAST-1 region.
**Lesson:** A manual operational command that can affect production capacity needs an enforced lower bound and a dry-run step, not just correct typing from the person running it.
**Source:** [Amazon: Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region](https://aws.amazon.com/message/41926/), March 2017.
**Cost:** L

### REL-003: TSB's bank migration landed with no way back
**Situation:** In April 2018, TSB Bank migrated roughly 5.4 million customer accounts from Lloyds' legacy platform to a new system (Proteo4UK) in a single "big bang" cutover rather than a staged rollout, without a workable rollback plan for if problems emerged after go-live. When the migration surfaced major defects, TSB could not revert to the old platform — it had already been decommissioned as part of the same release — and had to fix the new system live in production while customers were locked out of online and mobile banking, in some cases seeing other customers' account data or unable to access their own money.
**Impact:** Weeks of disrupted banking access for millions of customers; TSB was fined roughly £48.65 million by UK regulators, with total costs including compensation and remediation estimated above £330 million.
**Lesson:** "Deployed" isn't the same as "released safely" if there's no way back once something turns out to be broken. A cutover at this scale needs the old system kept live and reachable until the new one is proven, not decommissioned as part of the same go-live — reversibility has to be designed in before the migration starts, not improvised after it fails.
**Source:** [Slaughter and May: Independent Review of TSB's 2018 IT migration](https://www.slaughterandmay.com/news/slaughter-and-may-s-independent-review-of-tsb-s-2018-migration-to-a-new-it-platform/) (commissioned by the TSB Board), published November 19, 2019.
**Cost:** L

---

## RCK — Recheck

### RCK-001: GitLab trusted backups that had silently stopped working
**Situation:** During recovery from a January 31, 2017 database incident, GitLab discovered its `pg_dump` backup process had been failing for months. The backups ran with PostgreSQL 9.2 client binaries against a 9.6 database, on the wrong host, and failed silently; the failure emails were also being rejected by the receiving mail server over a DMARC signing issue, so nobody saw the failures either. Azure disk snapshots, the other safety net, weren't enabled for the database servers at all. Nobody had rechecked that any of the five backup mechanisms actually worked until they were needed.
**Impact:** A subsequent accidental deletion of the primary database's data directory (an engineer ran `rm -rf` on the wrong host while trying to fix replication lag) left GitLab able to recover from only a roughly six-hour-old snapshot; about 300GB of data and 6 hours of production changes were permanently lost.
**Lesson:** "We have backups" is a claim that goes stale the moment nobody has recently restored from one. Recheck that a safety mechanism is currently true, on a schedule, rather than trusting the fact that it was set up once.
**Source:** [GitLab: Postmortem of database outage of January 31](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/), February 10, 2017.
**Cost:** L

### RCK-002: An expired certificate took down Microsoft Teams for hours
**Situation:** On February 3, 2020, an authentication certificate used by Microsoft Teams expired. Independent monitoring from Exoprise detected the outage roughly 30 minutes before Microsoft's own status page acknowledged it. The public writeups do not show evidence of an automated pre-expiry check that would have caught this before it went live in production.
**Impact:** Around seven hours of degraded or unavailable service before a new certificate was rolled out at scale.
**Lesson:** An expiring credential is a predictable failure with a known date. A recheck against that date, days or weeks ahead, catches it for free; discovering it from a user-facing outage is the expensive way to find out.
**Source:** [Exoprise: Microsoft Teams Outage Due To Expired Certificate](http://www.exoprise.com/2020/02/04/teams-outage-expired-certificate/), February 2020.
**Cost:** M

### RCK-003: A signing certificate expired and took down every Firefox add-on
**Situation:** On May 4, 2019, the intermediate certificate Mozilla used to sign Firefox add-ons expired. Firefox's add-on system requires a valid signature chain before it will load an extension, so the moment the certificate's validity window ended, every already-installed signed add-on and theme stopped loading across Firefox's install base — with no code change and no attacker involved, the certificate had simply been valid and then wasn't. Mozilla's own post read: "We're deeply sorry for this occurrence. Currently the signature verification process is not working, causing all installed add-ons and themes to be disabled." Restoring service required pushing a new, valid certificate through the same update mechanism.
**Impact:** Roughly 15,000 add-ons disabled across Firefox's install base for around 15–21 hours for most users.
**Lesson:** An expiring credential is a scheduled failure with a known date already sitting on a calendar somewhere. If nothing rechecks that date ahead of the deadline and forces a renewal, the credential expires exactly on schedule and the "current" state everything downstream depends on silently becomes false.
**Source:** [Mozilla Add-ons Blog: Add-ons disabled or failing to install in Firefox](https://blog.mozilla.org/addons/2019/05/04/update-regarding-add-ons-in-firefox/), May 4, 2019.
**Cost:** L

### RCK-004: An expired certificate inside carrier software took down mobile data for millions
**Situation:** On December 6, 2018, a software certificate embedded inside Ericsson's SGSN-MME network element, a core piece of mobile data infrastructure used by carriers worldwide, expired. Because the certificate lived inside vendor software rather than being tracked as an externally-managed credential up for renewal, no process was rechecking its expiration date, and its expiry caused affected network nodes to fault simultaneously across every carrier running that software version. The resulting failures took down mobile data service for O2 in the UK, SoftBank in Japan, and carriers in several other countries at the same time.
**Impact:** O2 UK: roughly 16–24 hours of degraded or unavailable mobile data for millions of subscribers; SoftBank Japan: about 5 hours; 11 countries affected in total.
**Lesson:** A certificate embedded inside vendor software is still a certificate with an expiration date. If it isn't inventoried and rechecked against that date the same way externally-facing certificates are, its expiry surfaces for the first time as a live, simultaneous, multi-carrier outage instead of a routine renewal ticket.
**Source:** [TechCrunch: Here's what caused yesterday's O2 and SoftBank outages](https://techcrunch.com/2018/12/07/heres-what-caused-yesterdays-o2-and-softbank-outages/), December 7, 2018.
**Cost:** L

---

## RAT — Ratification

### RAT-001: FAA's delegated certification let Boeing self-certify MCAS
**Situation:** The FAA's Organization Designation Authorization program delegated large parts of the 737 MAX's certification, including review of the MCAS flight-control software, to Boeing's own employees acting on the FAA's behalf. The DOT Office of Inspector General's review of the certification timeline found the FAA had limited visibility into how MCAS changed in scope and authority over the course of development, and that Boeing did not give the FAA complete information about the system's later, more aggressive revision.
**Impact:** MCAS activated on faulty single-sensor data on two flights, Lion Air 610 (October 2018) and Ethiopian Airlines 302 (March 2019), killing 346 people combined; the 737 MAX fleet was grounded worldwide for about 20 months.
**Lesson:** Delegating sign-off to the people who built the thing isn't ratification, it's the same reviewer wearing two hats. A named, independent human has to actually see the full, current version of what they're approving.
**Source:** [DOT OIG: Weaknesses in FAA's Certification and Delegation Processes Hindered Its Oversight of the 737 MAX 8](https://www.oig.dot.gov/sites/default/files/FAA%20Certification%20of%20737%20MAX%20Boeing%20II%20Final%20Report%5E2-23-2021.pdf), February 2021.
**Cost:** L

### RAT-002: NASA overrode Thiokol engineers' recommendation not to launch Challenger
**Situation:** On the night of January 27, 1986, Morton Thiokol engineers formally recommended against launching Space Shuttle Challenger the next morning, because the solid rocket boosters' O-ring seals had never been tested or flown at the forecast freezing temperatures and were known to lose resiliency in cold. NASA managers at Marshall Space Flight Center pushed back on that recommendation during a teleconference, and Thiokol's own management then reversed its engineers' position and signed off on launch, overriding the technical objection to give NASA a clean "GO." Challenger launched the next morning, January 28, 1986, and broke apart 73 seconds after liftoff when a failed O-ring seal let hot gas escape.
**Impact:** All seven crew members were killed; the Space Shuttle program was grounded for 32 months.
**Lesson:** When the people with the technical standing to say "no" get overruled by the people who need the "yes," the sign-off has stopped tracking risk and started tracking organizational pressure. A ratification process only works if reversing an engineering recommendation requires clearing a higher bar of evidence than the recommendation itself, not just a louder room.
**Source:** Report of the Presidential Commission on the Space Shuttle Challenger Accident (the "Rogers Commission Report"), June 6, 1986; summarized at [NASA: Report of the Presidential Commission](https://www.nasa.gov/history/rogersrep/v1appa.htm).
**Cost:** L

### RAT-003: Japan's nuclear regulator rubber-stamped the industry's own safety assessments
**Situation:** Before the March 2011 Fukushima Daiichi accident, Japan's nuclear regulator (NISA) was housed inside the same government ministry responsible for promoting the nuclear industry, and its safety approvals routinely consisted of accepting utilities' own self-submitted assessments rather than independently verifying them. In one instance the Diet's investigation cited by name, NISA accepted TEPCO's 2009 anti-seismic assessment for a reactor even though the assessment covered only a fraction of the plant's safety-critical equipment. The independent National Diet of Japan Fukushima Nuclear Accident Independent Investigation Commission concluded the accident was fundamentally a result of this "regulatory capture," not simply a natural disaster.
**Impact:** A triple reactor meltdown following the March 11, 2011 earthquake and tsunami; over 150,000 people evacuated, with cleanup costs estimated in the hundreds of billions of dollars.
**Lesson:** A regulator that shares institutional incentives with the entity it's approving isn't ratifying anything, it's co-signing. Genuine sign-off requires an approver whose interest in saying "yes" is structurally weaker than their interest in being right — a stated policy of independence isn't enough if the org chart, funding, or mission ties the approver's success to the approved party's.
**Source:** [National Diet of Japan Fukushima Nuclear Accident Independent Investigation Commission: official report](https://www.nirs.org/wp-content/uploads/fukushima/naiic_report.pdf), July 5, 2012.
**Cost:** L

---

## REV — Review

### REV-001: Therac-25's software review never caught the race condition that overdosed patients
**Situation:** The Therac-25 radiation therapy machine, deployed starting 1985, removed hardware interlocks present in earlier models and relied entirely on software to prevent the beam from firing at the wrong dose or mode. A race condition let an operator's fast keyboard corrections desynchronize the software's internal state from the machine's actual configuration. Nancy Leveson and Clarke Turner's investigation found the software had never been independently reviewed or tested against realistic operator behavior; the company's own confidence came largely from the machine's field history on earlier hardware-interlocked models, not from a review of this software.
**Impact:** At least six confirmed massive radiation overdoses between 1985 and 1987, several fatal, before the pattern was identified and the machine recalled.
**Lesson:** A review that only checks whether code matches its design document, without an independent party exercising the real timing and inputs a human operator would produce, misses exactly the class of bug that comes from operators being faster or different than the design assumed.
**Source:** [Leveson & Turner: An Investigation of the Therac-25 Accidents](https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/therac25.pdf), IEEE Computer, 1993.
**Cost:** L

### REV-002: Parity's team reviewed a reported vulnerability and misjudged it as low-risk
**Situation:** In July 2017, Parity fixed one multi-sig wallet vulnerability by deploying a new version of its wallet library contract — but that new version had a separate flaw: because the library's functions were directly callable, anyone could call its `initWallet` function and become the owner of the shared library itself, not just of an individual wallet. In August 2017, a GitHub user reported this exact risk; Parity's team reviewed the report but assessed it as not warranting action. On November 6, 2017, a user triggered the flaw (not maliciously), became owner of the library, and then deleted it — and because every multi-sig wallet built on that library delegated its logic to it rather than holding its own code, deleting the shared library permanently froze the funds in every wallet depending on it.
**Impact:** Hundreds of multi-sig wallets permanently lost access to their funds; contemporaneous reporting valued the frozen ETH at roughly $150–300 million depending on when the estimate was taken.
**Lesson:** A reported risk that gets reviewed and dismissed has failed exactly as thoroughly as one that was never reported, if the review doesn't correctly weigh what's actually at stake — here, that the flaw sat in a single shared library every wallet delegated to, not in an isolated per-wallet contract. When a report's severity depends on understanding the blast radius of the underlying architecture, route it to someone who can actually assess that, not just whoever triages the queue.
**Source:** [Parity Technologies: A Postmortem on the Parity Multi-Sig Library Self-Destruct](https://medium.com/paritytech/a-postmortem-on-the-parity-multi-sig-library-self-destruct-63daca3a4cf7), November 2017; corroborated by [CoinDesk: Parity Team Publishes Postmortem on $160 Million Ether Freeze](https://www.coindesk.com/markets/2017/11/15/parity-team-publishes-postmortem-on-160-million-ether-freeze), November 15, 2017.
**Cost:** L

---

## REC — Recall

No real, specific public postmortem has turned up in two separate search passes (initial draft, and a follow-up pass focused specifically on this category) that cleanly isolates a "failed to recall or reuse known prior work" failure mode the way the other categories did. Candidates considered and rejected as too weak a fit: GitLab's team lacking accessible runbooks during replication recovery (better classified under RCK, the category it's already used in); a second exploit against Litecoin's MWEB reusing a prior attack path before a full codebase audit was complete (better classified as an incomplete REV/RCK than a recall failure). Leaving this empty rather than stretching a source past what it actually documents. Worth a dedicated pass with different search terms — internal engineering retrospectives about duplicated tooling are more likely to exist as internal docs than public blog posts, which may be why this category is structurally underrepresented in public postmortem writing regardless of how common the failure is in practice.

---

## FAI — Failure Analysis

FAI isn't a separate incident type in this draft; it's the lens applied to any item above when you're extracting the general, transferable pattern rather than the fix. All items above already qualify as FAI-tagged material under their primary ability code.
