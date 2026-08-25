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

---

## RAT — Ratification

### RAT-001: FAA's delegated certification let Boeing self-certify MCAS
**Situation:** The FAA's Organization Designation Authorization program delegated large parts of the 737 MAX's certification, including review of the MCAS flight-control software, to Boeing's own employees acting on the FAA's behalf. The DOT Office of Inspector General's review of the certification timeline found the FAA had limited visibility into how MCAS changed in scope and authority over the course of development, and that Boeing did not give the FAA complete information about the system's later, more aggressive revision.
**Impact:** MCAS activated on faulty single-sensor data on two flights, Lion Air 610 (October 2018) and Ethiopian Airlines 302 (March 2019), killing 346 people combined; the 737 MAX fleet was grounded worldwide for about 20 months.
**Lesson:** Delegating sign-off to the people who built the thing isn't ratification, it's the same reviewer wearing two hats. A named, independent human has to actually see the full, current version of what they're approving.
**Source:** [DOT OIG: Weaknesses in FAA's Certification and Delegation Processes Hindered Its Oversight of the 737 MAX 8](https://www.oig.dot.gov/sites/default/files/FAA%20Certification%20of%20737%20MAX%20Boeing%20II%20Final%20Report%5E2-23-2021.pdf), February 2021.
**Cost:** L

---

## REV — Review

### REV-001: Therac-25's software review never caught the race condition that overdosed patients
**Situation:** The Therac-25 radiation therapy machine, deployed starting 1985, removed hardware interlocks present in earlier models and relied entirely on software to prevent the beam from firing at the wrong dose or mode. A race condition let an operator's fast keyboard corrections desynchronize the software's internal state from the machine's actual configuration. Nancy Leveson and Clarke Turner's investigation found the software had never been independently reviewed or tested against realistic operator behavior; the company's own confidence came largely from the machine's field history on earlier hardware-interlocked models, not from a review of this software.
**Impact:** At least six confirmed massive radiation overdoses between 1985 and 1987, several fatal, before the pattern was identified and the machine recalled.
**Lesson:** A review that only checks whether code matches its design document, without an independent party exercising the real timing and inputs a human operator would produce, misses exactly the class of bug that comes from operators being faster or different than the design assumed.
**Source:** [Leveson & Turner: An Investigation of the Therac-25 Accidents](https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/therac25.pdf), IEEE Computer, 1993.
**Cost:** L

---

## REC — Recall

No real, specific public postmortem has turned up in two separate search passes (initial draft, and a follow-up pass focused specifically on this category) that cleanly isolates a "failed to recall or reuse known prior work" failure mode the way the other categories did. Candidates considered and rejected as too weak a fit: GitLab's team lacking accessible runbooks during replication recovery (better classified under RCK, the category it's already used in); a second exploit against Litecoin's MWEB reusing a prior attack path before a full codebase audit was complete (better classified as an incomplete REV/RCK than a recall failure). Leaving this empty rather than stretching a source past what it actually documents. Worth a dedicated pass with different search terms — internal engineering retrospectives about duplicated tooling are more likely to exist as internal docs than public blog posts, which may be why this category is structurally underrepresented in public postmortem writing regardless of how common the failure is in practice.

---

## FAI — Failure Analysis

FAI isn't a separate incident type in this draft; it's the lens applied to any item above when you're extracting the general, transferable pattern rather than the fix. All items above already qualify as FAI-tagged material under their primary ability code.
