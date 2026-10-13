# Module 0 · Orientation & baseline
import html as _html
import os as _os

# 0.3 runs the AI readiness diagnostic prompt from teamempathy.co.nz/community.
# Kept in diagnostic_prompt.txt; build.py warns if the community page drifts.
DIAGNOSTIC_PROMPT = _html.escape(open(_os.path.join(_os.path.dirname(__file__), "diagnostic_prompt.txt")).read().strip(), quote=False)

LESSONS = [
{
"id": "0.1",
"slug": "0-1-the-new-rules-of-discovery",
"title": "The new rules of discovery",
"h1": 'The new rules of <span class="te-editorial">discovery</span>',
"description": "How people find ecommerce brands has changed shape. Zero-click, AI shopping, and the entity-confidence thesis: in 2026 you optimise to become the brand AI recommends, not to rank a page.",
"tag": "Foundational",
"mins": 7,
"lead": "The shift in how people find ecommerce brands, before we get to any tactics. Read this once, then forward it to anyone on your team who needs the same starting point.",
"body": """
    <h2>The shift</h2>
    <p>Search has changed shape.</p>
    <p>For twenty years, "search" meant typing a few words into Google, looking at ten blue links, and clicking through to read the answer yourself. That is not how most product research happens now. People ask ChatGPT, Perplexity, Claude, or Google's AI Overviews a full question, like "what's the best magnesium glycinate for sleep" or "comfortable trainers for plantar fasciitis under $200", and get a direct answer back. Often with a shortlist of brands. Often without ever clicking a link.</p>
    <p>The numbers behind it are not subtle:</p>
    <ul>
      <li>ChatGPT sent ecommerce brands <strong>1,079% more shopping traffic last year</strong> than the year before. <span class="src">(Visibility Labs / Search Engine Land)</span></li>
      <li>On Shopify specifically, AI-driven traffic is up <strong>8x</strong> and AI-driven orders up <strong>15x</strong> since January 2025. <span class="src">(Kyle Risley, Senior SEO Lead at Shopify, 2026)</span></li>
      <li>Visitors from AI platforms convert <strong>31% better</strong> than non-branded organic. <span class="src">(Profound, 94 brands tracked, 2025)</span></li>
    </ul>
    <p>This is the current state of how purchase research happens for a serious slice of your category. 61% of consumers have already used an AI tool to research a purchase, and 64% say they plan to do more of it this year. <span class="src">(Adobe Analytics; Shopify, 2026)</span> The traffic models that built the last decade of ecommerce are being replaced by something different.</p>

    <h2>What you're actually optimising for now</h2>
    <p>This is the mental shift the whole Playbook hinges on:</p>
    <div class="pullquote">
      <span class="label">The thesis</span>
      <p>In 2026, you are not optimising for a ranking algorithm. You are optimising to become the entity AI systems have the highest confidence in recommending for your category.</p>
    </div>
    <p>That is a structural change. The old job was making one page rank higher than another for one keyword. The new job is making your brand the answer an AI gives when someone asks a question about your category. Shopify APAC's Director of Partnerships puts it the same way:</p>
    <blockquote class="quote">
      <p>"Search is becoming a conversation, and commerce is becoming agentic. In 2026, visibility is less about being the loudest, and more about being the easiest for machines to understand and trust."</p>
      <cite>Rhys Furner, Shopify APAC</cite>
    </blockquote>
    <p>AI returns the answer. The first brand it names is the brand the customer considers first.</p>
    <p><strong>93% of AI search sessions now end without anyone clicking through to a website.</strong> <span class="src">(AirOps 2026 State of AI Search Report)</span> The consideration set is decided inside the AI before you would traditionally know the customer existed.</p>
    <p>Everything else in this Playbook, the technical foundations, the content engine, the reviews, the digital PR, the Reddit work, the LinkedIn presence, all of it builds the confidence AI has in recommending your brand.</p>

    <h2>Why this is the 2011 window all over again</h2>
    <p>Think about who won SEO between 2011 and 2015. The brands that built the asset early, while it was still cheap to do. They compounded for a decade. They paid less and less for traffic while everyone else paid more.</p>
    <p>The same window is open right now, just one platform shift further on.</p>
    <p>The brands that install AI search visibility in 2026 will quietly compound past competitors who are still trying to outspend their way to growth. Most founders have not priced this into their growth model yet. That is the opportunity.</p>

    <h2>Paid is rented. Search and AI is owned.</h2>
    <p>Paid ads work while you spend. The day you stop, it stops. CACs are creeping. MERs are flattening. The maths gets harder every quarter.</p>
    <p>Search and AI visibility is the opposite shape of asset. Built once, refreshed quarterly, it keeps sending qualified buyers month after month, year after year. The asset compounds. The cost does not.</p>
    <p>That is the system the Playbook teaches you to build.</p>
""",
"donow": [
"Ask ChatGPT a buying question in your category: \"best [your product] for [use case]\". Do you pop up? Note which brands it names. Those are the brands you're up against for AI visibility, and by the end of this playbook you'll know exactly how to join them.",
"Then ask it straight: \"What do you know about [your brand]?\" What it gets wrong, or doesn't know at all, is your starting point.",
],
"prompt": """Act as an AI search analyst. For my store [URL], list the ten questions a buyer in my category would ask ChatGPT or Perplexity before purchasing, and note whether my brand is likely to be named in the answer today.""",
"app": True,
},
{
"id": "0.2",
"slug": "0-2-your-score-out-of-100",
"title": "Where you stand: your score out of 100",
"h1": 'Where you stand: your score out of <span class="te-editorial">100</span>',
"description": "Score your store against the AEO Maturity Model: four pillars, five levels, 100 points. Certified is 80. Here's how to place yourself honestly before you change a thing.",
"tag": "Baseline",
"mins": 8,
"lead": "Before you fix anything, you need an honest number. This lesson gives you the exact scoring model we use with our own clients, so you know where you're starting from and can prove how far you've come.",
"body": """
    <h2>The AEO Maturity Model</h2>
    <p>We score every store we work with out of 100, using a model built on the same four pillars as this playbook. Each pillar gets a level from 1 to 5, worth 5 points per level. So each pillar is worth up to 25 points, and the four together make 100.</p>
    <ul>
      <li><strong>Technical</strong>, can AI read you?</li>
      <li><strong>Content</strong>, do you answer the questions buyers ask?</li>
      <li><strong>Authority</strong>, do the engines trust you?</li>
      <li><strong>Measurement</strong>, can you see it working?</li>
    </ul>
    <p>The five levels are the same for every pillar: <strong>Invisible</strong> (1), <strong>Emerging</strong> (2), <strong>Structured</strong> (3), <strong>Professional</strong> (4), and <strong>Leading</strong> (5).</p>
    <div class="pullquote">
      <span class="label">The target</span>
      <p>Certified AI-Ready is Professional on all four pillars. That's 80 out of 100, and it's the number this whole playbook is built to get you to.</p>
    </div>

    <h2>What each level actually looks like</h2>
    <p>Here's the honest version, pillar by pillar. Score yourself as you read.</p>
    <p><strong>Technical.</strong> Invisible means AI crawlers are blocked and there's no schema. Emerging loads fine but has no structured data. Structured has core schema on key pages with gaps. Professional has valid schema, crawlers welcomed, and Core Web Vitals passing. Leading is rich, entity-linked schema monitored continuously.</p>
    <p><strong>Content.</strong> Invisible is product pages only, nothing an AI could quote. Emerging has a few posts that aren't answer-first. Structured has some real answers and an FAQ. Professional has a topic-cluster roadmap with cornerstone pieces AI actually quotes. Leading is a compounding engine that gets cited consistently.</p>
    <p><strong>Authority.</strong> Invisible has almost no off-site signals. Emerging has a handful of links, nothing managed. Structured has consistent core citations but it's ad hoc. Professional has quality backlinks, a clean profile, and strong reviews. Leading has earned press and genuine category authority.</p>
    <p><strong>Measurement.</strong> Invisible has no baseline and no tracking. Emerging has analytics installed that nobody looks at (this is most stores, honestly). Structured checks occasionally with no rhythm. Professional has a baseline plus a share-of-voice framework on a cadence. Leading has a live dashboard tied to action.</p>

    <h2>Score yourself now</h2>
    <p>Most Shopify stores we score for the first time land somewhere between 35 and 50. That's normal, and it's good news: the gap between where you are and 80 is exactly what this playbook closes, module by module.</p>
    <p>Be harsh with yourself. A generous self-score just hides the wins you could be collecting. If you're straddling two levels on a pillar, take the lower one. The gating rule we use with clients: if any requirement of the higher level is missing, you're not there yet.</p>
    <p>Write your four numbers down somewhere you'll keep. Your total is your baseline, and in Module 4 you'll re-score against it to prove the progress.</p>
""",
"donow": [
"Score each pillar 1 to 5, multiply each by 5, and add them up. Write down the four pillar scores and the total, plus today's date. That number is your baseline.",
"Want it done properly? <a href=\"https://teamempathy.co.nz/scorecard\">Get your free score here</a>. It runs a live scan of your store and scores all four pillars for you.",
],
"app": True,
},
{
"id": "0.3",
"slug": "0-3-plug-claude-into-your-store",
"title": "Plug Claude into your store",
"h1": 'Plug Claude into your <span class="te-editorial">store</span>',
"description": "Give Claude your Search Console, GA4 and Shopify numbers, then run the AI readiness diagnostic prompt. It builds your own Search & AI readiness report: your score out of 100, the market you're missing, and what it's worth in dollars.",
"tag": "Setup",
"mins": 8,
"lead": "This is where the playbook stops being theory. Fifteen minutes gathering your own numbers, one prompt, and Claude builds you the same kind of readiness report we build for clients.",
"body": """
    <h2>Why your own data changes everything</h2>
    <p>In 0.1 you asked ChatGPT about your category. In 0.2 you scored yourself. Both are useful, and both are guesses.</p>
    <p>Your own numbers aren't. Search Console shows exactly which searches your store already appears for. GA4 and Shopify show what that traffic is worth. Hand those to Claude with the right prompt and it stops guessing about your store and starts working from what actually happened on it.</p>
    <p>That's what this lesson does. It's the same diagnostic prompt we hand out in our community, and it produces a proper report: where you stand, the demand you're missing, and the first things to fix.</p>

    <h2>Step 1: gather your numbers</h2>
    <p>You need three things. Screenshots are fine; exports are better.</p>
    <ol>
      <li><strong>Google Search Console.</strong> Open Performance, then Search results. Set the date range to the last 12 months, then hit Export and download the CSV. The Queries and Pages tabs are the ones that matter. This is the most important file of the three.</li>
      <li><strong>GA4.</strong> Open Reports, then Acquisition, then Traffic acquisition, set to the last 12 months. Screenshot it so Claude can see sessions and revenue by channel, especially Organic Search.</li>
      <li><strong>Shopify.</strong> Open Analytics and screenshot the overview for the last 12 months: total sales, sessions and conversion rate. If you can, add the sessions and sales by referrer reports too.</li>
    </ol>
    <p>No Search Console yet? Set it up today (it's free, and lesson 1.9 explains why it matters) and run the prompt anyway. Claude will work from what it can see and tell you what's missing.</p>

    <h2>Step 2: keep it safe</h2>
    <ul>
      <li><strong>Share numbers, never logins.</strong> Claude only ever needs the exports and screenshots. It never needs your passwords or admin access.</li>
      <li><strong>Read-only, always.</strong> Nothing in this lesson changes your store. You're giving Claude something to read.</li>
      <li><strong>Use your own Claude account.</strong> Your data stays in your conversation.</li>
    </ul>

    <h2>Step 3: run the diagnostic prompt</h2>
    <p>Open a new Claude chat and make sure web search is switched on, so Claude can look at your live site (your robots.txt, your product pages, your blog). Attach your three files, copy the prompt below, fill in the brand details at the top, and send it.</p>
    <p>It works through seven steps, the same way we work through a store for a client:</p>
    <ol>
      <li>Inspects your site the way an AI search engine would.</li>
      <li>Splits your searches into branded and non-branded, because non-branded is the market you can actually grow.</li>
      <li>Sizes your market from free, real data, labelling every number measured or estimated.</li>
      <li>Tests your AI visibility directly, with ten buyer questions.</li>
      <li>Scores you out of 100 on the four pillars from 0.2.</li>
      <li>Builds a money model from your own numbers.</li>
      <li>Writes it all up as a five-section report.</li>
    </ol>
    <p>Give it a few minutes. When it's done, save the conversation. Lesson 0.4 walks you through reading it properly.</p>
""",
"donow": [
"Export your Search Console data, screenshot GA4 and Shopify, then run the prompt below in Claude with all three attached. Save the report it gives you; it's the starting point for the rest of the playbook.",
"Then bring your report into the <a href=\"https://teamempathy.co.nz/community\">free community</a>, and we'll tell you what we'd do first.",
],
"prompt_label": "The AI readiness diagnostic prompt",
"prompt": DIAGNOSTIC_PROMPT,
"app": True,
},
{
"id": "0.4",
"slug": "0-4-read-your-report",
"title": "Read your report in detail",
"h1": 'Read your report in <span class="te-editorial">detail</span>',
"description": "Walk through your Search & AI readiness report section by section: the score, the market you're missing, the money model and the five actions. Pressure-test it, then turn it into your plan for the rest of the playbook.",
"tag": "Baseline",
"mins": 8,
"lead": "You've got a report. Now read it like a strategist would: check what's measured and what's estimated, find the one number that matters most, and turn the five actions into your plan for the modules ahead.",
"body": """
    <h2>Before you read: measured or estimated?</h2>
    <p>Every number in your report should be labelled. <strong>Measured</strong> means it came straight from your data, like Search Console impressions or GA4 revenue. <strong>Directional</strong> or <strong>modelled</strong> means Claude estimated it.</p>
    <p>Both are useful, but they carry different weight. Make decisions on the measured numbers and treat the estimates as a sense of scale. If a number has no label, ask Claude where it came from before you lean on it.</p>

    <h2>1. The executive summary</h2>
    <p>Three things to know, then the scenario table: Today, Conservative, Mid and High. Look at the gap between Today and Conservative first. Conservative is the version you should plan around. High is what it looks like if everything goes right, so don't build your budget on it.</p>

    <h2>2. How AI-ready you are today</h2>
    <p>Your score out of 100 across the four pillars. Put it next to the score you gave yourself in 0.2. If they're miles apart, find out why: usually you've been generous on a pillar, or Claude couldn't see something you know about.</p>
    <p>Each pillar points to part of this playbook:</p>
    <ul>
      <li><strong>Technical</strong> is Module 1.</li>
      <li><strong>Content</strong> is Module 2.</li>
      <li><strong>Authority</strong> is Module 3.</li>
      <li><strong>Measurement</strong> is Module 4.</li>
    </ul>
    <p>Your lowest pillar is the module that will pay you back fastest. 80 is AI-ready, and that's the target.</p>

    <h2>3. The market you're missing</h2>
    <p>This is the section most people skim, and it's the one that matters most. Check the branded vs non-branded split. Branded searches are people who already know you, and no strategy grows them much. Non-branded is everyone shopping your category who hasn't found you yet. That's the market you can win.</p>
    <p>Look at which non-branded searches you already appear for, and where you rank. Searches where you're sitting on page two are the closest wins in the whole report.</p>

    <h2>4. The opportunity, in dollars</h2>
    <p>Three numbers to find:</p>
    <ul>
      <li><strong>The value of a non-branded click.</strong> What one visitor from a category search is worth to you.</li>
      <li><strong>Your share of the market today.</strong> How much of the winnable pool you already hold.</li>
      <li><strong>The value of each extra 1% of share.</strong> This is the number to remember. It tells you what the work is worth before you start it.</li>
    </ul>
    <p>Sanity-check it. Your branded revenue should sit on top, untouched. Any share above 25% should be flagged as a stretch. If the dollar columns are marked directional, the report should tell you which piece of data would firm them up, so go and get it.</p>

    <h2>5. What to do next</h2>
    <p>Five actions in priority order. Match each one to the lesson that covers it: blocked AI crawlers is 1.1, missing product schema is 1.4, empty collection pages is 1.5, no content answering buyer questions is Module 2, not enough reviews or mentions is Module 3. That list, in that order, is your path through the playbook.</p>

    <h2>Pressure-test it</h2>
    <p>Claude can be wrong, so check two things yourself before you act. Open yourstore.com/robots.txt and confirm what it said about the AI crawlers. Then ask ChatGPT two or three of the buyer questions from the AI visibility test and see whether the answers match. If something doesn't line up, tell Claude and ask it to rework that section.</p>
""",
"donow": [
"Read the report section by section. Write down four things: your score out of 100, your lowest pillar, the value of an extra 1% of market share, and the five actions in order. Then run the prompt below in the same Claude chat to turn them into your plan.",
"Stuck on something in your report? Bring it into the <a href=\"https://teamempathy.co.nz/community\">free community</a>.",
],
"prompt": """Now turn this report into my action plan for The AI Search Playbook. The playbook has four modules: Module 1 Technical foundations (crawler access, Shopify URLs, product pages, product schema and GTINs, collections, internal links, merchant feeds, speed), Module 2 Content (buying-intent keywords, topic clusters, buying guides, refreshing content), Module 3 Authority (reviews, review platforms, Reddit and forums, digital PR, founder presence) and Module 4 Measurement.

1. For each of the five actions in the report, tell me which module covers it and why it's in that position.
2. Tell me which numbers in the report are measured and which are estimates, and which estimate I should firm up first.
3. Give me the order to work through the modules, starting with my lowest-scoring pillar, and the first three things to do this week.""",
"app": True,
},
]
