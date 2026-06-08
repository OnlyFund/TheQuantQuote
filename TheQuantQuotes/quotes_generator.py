"""
Trading quotes generator for derivatives and volatility markets.
Investment bank options desk humor and wisdom.
"""
import random
from typing import List
from collections import deque

# Collection of trading wisdom and options desk humor
TRADING_QUOTES = [
    # Gamma
    "Gamma kills, but theta heals",
    "Short gamma, long trauma",
    "Theta pays the rent, Gamma takes the house",
    "Friends don't let friends sell naked gamma",
    "Gamma: the silent portfolio killer",
    "In gamma we trust, in delta we adjust",
    "Gamma scalping: because sleep is overrated",
    "Vol Risk Premium: good luck capturing that...",
    "Long gamma, short sanity",
    "A 1Δ option on the day of expiry: the stuff traders' nightmares are made of",
    "Stoch-Local Vol is not a model choice, it's a commitment issue",
    "Every time that an axe gets filled, a sales trader gets his wings",
    "USDJPY drops 1% - maybe something, probably nothing",
    'Zero: the only true answer to the question "How low vols can go"',
    'Short vol smile - the lifespan of a Thanksgiving turkey',
    'Long gamma, short patience',
    "Gamma is just leverage wearing glasses",
    "Short gamma, long explanations",
    "Gamma exposure: choose violence",
    "Gamma hedge completed, disaster postponed",
    "Every gamma trade starts as a good idea",
    "Long gamma, short career expectancy",
    "Gamma doesn't care about your thesis",
    "The market giveth, gamma taketh away",
    "Gamma is temporary, screenshots are forever",
    "Gamma is Nemesis — punishment for imbalance",
    "Short gamma at 9am, short career by 4pm",
    "Gamma neutral on paper, anything but in practice",
    "The gamma spike always finds the unhedged book",
    "Every vol seller discovers their gamma limit eventually",

    # Basis
    "When basis explodes, pods implode",
    "Basis risk: physical reality's revenge on financial models",
    "When basis gaps, P&L snaps",
    "Basis moves are measured in cents and felt in millions",
    "Every blowout starts with 'that's cheap'",
    "Basis is just correlation breaking with conviction",
    "Storage full, basis cruel",
    "When basis explodes, VAR discovers geography",
    "Location spreads: same barrel, different disaster",
    "Basis traders don't predict weather, they price it",
    "Every basis trade is a liquidity trade in disguise",
    "The basis always knows something",
    "Basis: where logistics become volatility",
    "When pipelines fill, basis pays the bill",
    "Flat price is a view, basis is a surprise",
    "Basis moves first, explanations follow later",
    "Basis widened 20 cents, careers narrowed considerably",
    "Basis risk: because flat price wasn't painful enough",
    "Basis blowup: when the model assumed frictionless transport",
    "Basis is the market's way of reminding you that geography exists",

    # Vega
    "Vega hurts when you least expect it",
    "Long vega, short nerves",
    "Vega Hurts, Gamma Kills",
    "When vega spikes, portfolios dive",
    "Vega P&L: now featuring random numbers",
    "Vega always moves after you've hedged it",
    "Long vega, short confidence",
    "Vega is just gamma with extra steps",
    "Vega doesn't hurt until it does",
    "Vega convexity: expensive and misunderstood",
    "Vega hedged at open, vol surface repriced by lunch",
    "Long vol: eventually correct, immediately unemployed",
    "Short vol: collecting premiums from future you",

    # Theta
    "Theta decay: the only certainty in options",
    "Time is money, theta is proof",
    "Theta never sleeps, neither do option sellers",
    "Theta: slow violence",
    "Theta positive, life negative",
    "Weekend theta: the gift that keeps on giving",
    "Theta never misses payroll",
    "Theta harvest season",
    "Time decay: undefeated since forever",
    "Theta is the internship of P&L",
    "Theta: charging rent on borrowed hope",
    "Every option expires worthless eventually",
    "Theta positive, emotionally negative",

    # Delta
    "Delta neutral, emotionally unstable",
    "Delta hedging: the art of controlled panic",
    "Delta one, problems none",
    "Delta hedging: because picking a direction is hard",
    "Your delta is showing",
    "Delta was never the problem",
    "Delta hedge first, ask questions later",
    "Delta: the gateway Greek",
    "Flat delta, not flat emotions",
    "The market chose a direction for me",
    "Delta is temporary, slippage is forever",
    "Delta hedging: solving today's problem tomorrow",
    "Spot moved. There goes the hedge.",
    "Your directional view is showing",

    # FX Vol
    "FX vol: where central banks ruin your day",
    "Cable vol: Brexit's eternal gift",
    "EM FX vol: because you hate stability",
    "Spot moves 5%, vol moves 50%, desk moves to new jobs",
    "Carry trade: because we all love free money",
    "FX options: where 25 delta means something",
    "Butterfly spread: for when you're wrong about everything",
    "Vol surface: flat in theory, bumpy in practice",
    "Eskimos have 4 different ways of saying snow, FX has 4 different ways of saying ATM strike",
    "Premium-adjusted delta: because regular delta was too simple",
    "ATMF vs ATMS: fighting over basis points",
    "Flat smile: said no FX trader ever",
    "FX vol quotes: bid-offer wider than the smile",
    "EM carry unwind: 3 months of carry, 3 hours of losses",
    "G10 vol: boring until it's not, and then it's really not",
    "Central bank intervention: the event vol you can't delta hedge",
    "FX forward points: carry that never feels free",

    # Options desk
    "Marked my book, marked my soul",
    "P&L explain: creative writing for traders",
    "Model says buy, gut says sell, compliance says no",
    "Hedged my Greeks, forgot my sanity",
    "Bid-offer spread: how wide can we go?",
    "Month-end: when everyone pretends to care about risk",
    "Unwind that position? But it's my favorite loser",
    "Nothing is more permanent than a temporary hedge",
    "The trade looked better yesterday",
    "The book is balanced, the trader isn't",
    "P&L explain pending divine intervention",
    "If you can't explain the P&L, neither can they",
    "The ticket never lies, people do",
    "Every clean book has a messy history",
    "Middle office knows where the bodies are buried.",
    "That 'small position' has a funny way of growing.",
    "Risk says no. Trader says 'just this once'.",
    "What could go wrong usually does... in settlement.",
    "Ops doesn't sleep, it just finds new breaks.",
    "A 'sure thing' is just a delayed problem.",
    "The desk is calm right before it isn't.",
    "Hedging is Sisyphus work: correct, exhausting, never finished.",
    "Flow desk: the trading floor's memory",
    "Axe gone. Spread blown. Sales apologises later.",
    "Book handed over at month-end with a wink and a prayer",
    "The risk limit exists until a good client calls",
    "Structured product closed. Residual risk opened.",
    "Unwind request at 3:55pm on an illiquid Friday",

    # Volatility
    "Low vol kills, high vol thrills",
    "Implied vol is just expensive hope",
    "Realized vol: where predictions go to die",
    "Volatility: can't live with it, can't trade without it",
    "Vol of vol: because one layer of complexity wasn't enough",
    "Sticky strike, sticky delta, sticky P&L",
    "Vol clustering: bad news travels in packs",
    "Vol risk premium: gap between fear and reality",
    "Vol compression: trader depression",
    "Vol expansion: nature healing",
    "Vol mean reversion: eventually, maybe, hopefully",
    "Realized-implied spread: the trade that never works",
    "Long vol: right eventually, broke immediately",
    "Short vol: profitable until it's catastrophic",
    "Vol regime change: when your model breaks",
    "Forward vol: today's uncertainty about tomorrow's uncertainty",
    "Short vol in a low-vol regime: picking up nickels, not dimes",
    "Vol carry works until the event everyone forgot about",
    "Selling vol: great strategy, terrible timing, every time",

    # Skew / Risk Reversal
    "Skew happens",
    "Skew trade: right direction, wrong timing, no P&L",
    "If you like our 25-delta RR, you will LOVE our 10-delta",
    "Skew is fear with decimal places",
    "The smile is smiling at your losses",
    "Skew remembers every crisis",
    "Every surface is arbitrage-free until inspected",
    "The wings know things",
    "Surface calibrated, reality uncooperative",
    "The surface moved because it felt like it",
    "Local vol, global pain",
    "Every skew trade becomes a timing trade",
    "Smile fitting: curve fitting with consequences",
    "Put skew: always expensive, sometimes worth it",
    "Skew carry: collecting pennies, risking dollars",
    "Risk reversal: the market's fear gauge",
    "Skew flattening: selling high, buying higher",
    "Skew steepening: when markets panic",
    "The smile is Delphi — always ambiguous, always right in hindsight",
    "The wings aren't rich enough",
    "Skew steepens at the worst moment to be short it",
    "25d risk reversal: the desk's daily mood ring",
    "The 10-delta put knows things the ATM doesn't",

    # Greeks general
    "The only Greek that matters is the P&L",
    "Hedge early, hedge often, still lose money",
    "Convexity: expensive insurance you hope to never use",
    "Correlation goes to one when you need it least",
    "Greeks are theoretical, losses are real",
    "One more Greek should fix this",
    "There is always another Greek",
    "The Greeks send their regards",
    "Greek-neutral, problem-positive",
    "The hedge has hedges now",
    "Greeks explained everything except the losses",
    "Cross-greeks: collaborative suffering",
    "Higher-order Greeks, lower-order judgment",
    "Know your Greeks, lose money anyway",
    "Greeks: named by mathematicians, feared by traders",
    "The Greeks always had a thing with tragedies",
    "First-order Greeks: what you hedge. Second-order Greeks: what kills you",
    "Greeks report: 47 pages of numbers, zero insight",
    "Greek letters: because English wasn't confusing enough",
    "Greeks neutral: theoretically possible, practically impossible",
    "Greeks dashboard: red everywhere, explanations nowhere",
    "Managing Greeks: like juggling chainsaws, blindfolded",
    "Greeks in crisis: all positive, portfolio still negative",
    "The Greek alphabet: 24 letters, infinite ways to lose money",
    "Every position is a hedge against happiness",
    "The Greeks: ancient wisdom, modern pain",

    # Vanna / Volga / Charm
    "Vanna: when your delta hedge needs a hedge",
    "Vanna risk: gamma's evil twin",
    "Long vanna, short explanations to risk managers",
    "Vanna/Volga - never worth it, always painful",
    "Vanna/Volga Greeks: calculated to the fifth decimal, wrong to the first",
    "Vanna exposure: when spot and vol move together, you lose twice",
    "Volga: gamma for vol traders",
    "Vomma: the Greek that breaks your vol models",
    "Short volga, short sleep",
    "Short Cross-Gamma: because shock therapy isn't working anymore",
    "Charm: theta's derivative, trader's nightmare",
    "Charm decay: when your delta hedge expires",
    "Monitoring charm at month-end: a special kind of masochism",
    "Color: gamma's gamma, sanity's enemy",
    "Hedging color? Just close the position",
    "Zomma: the Greek that sounds made up",
    "Higher-order Greeks: job security for quants",
    "Greeks beyond delta: diminishing returns, increasing confusion",
    "Managing cross-gamma: a fool's errand",
    "Vanna is just the market's way of saying your hedge was wrong in two dimensions",
    "Volga hedging: opened the textbook, closed the position",
    "Cross-vanna: two underlyings, four explanations, one loss",

    # Barrier options
    "Barrier options: because vanilla is too boring",
    "Knock-in, knock-out, knock yourself out",
    "Barrier breach at 2:59pm? Classic",
    "One-touch option: touched once, regretted forever",
    "Don't care about the terminal distribution, give me the whole damn path",
    "American barriers: can breach anytime, will breach at worst time",
    "Barrier monitoring: continuous in theory, discrete in practice, painful always",
    "Double barrier: twice the risk, half the premium",
    "Window barriers: barrier only matters sometimes, pricing matters always",
    "Barrier gamma spike: the path-dependent version of stepping on a Lego",
    "Rebate: consolation prize nobody wanted",
    "Reverse knock-out: because hedging it is worse than holding it",

    # Exotics & Structured Products
    "Exotic options: where closed-form solutions go to die",
    "Structured products: complexity for fees, simplicity for losses",
    "Exotic pricing: Monte Carlo until it works",
    "Path dependency: history matters, models don't care",
    "Structured notes: sold not bought",
    "Exotic options desk: where quants become traders and traders become alcoholics",
    "Term sheet: 40 pages of ways to lose money",
    "Payoff diagrams: beautiful in PowerPoint, ugly in P&L",
    "TARFs: target redemption, actual destruction",
    "Accumulators: I will kill you later",
    "Autocallables: early redemption for the house, bag holding for you",
    "Worst-of options: because someone hates you",
    "Variance swaps: pure vol exposure, impure P&L",
    "Dispersion trades: long single-name vol, short index vol, short sanity",
    "Asian options: because one fixing wasn't painful enough",
    "Lookback options: hindsight is 20/20, pricing is impossible",
    "Pricing exotics: garbage in, garbage out, fees in between",
    "Calibration: fitting wrong models to bad data",
    "Monte Carlo convergence: eventually wrong with confidence",
    "Digital options: zero or hero, mostly zero",
    "Digital gamma: infinite in theory, painful in practice",
    "Exotic sales pitch: 'It's like a vanilla option, but...'",
    "Structuring desk: creating problems for traders to solve",
    "Exotic bid-offer: wide enough to drive a truck through",
    "Quanto options: FX risk you didn't know you had",
    "Bermudan options: American freedom with European restrictions",
    "Callable bonds: issuer's option, investor's problem",
    "Cliquet vol: ratcheting volatility, ratcheting pain",
    "FX TARFs: sold to corporates, hedged by traders, understood by nobody",
    "Power reverse dual currency: words that mean nothing, losses that mean everything",
    "Static replication: works in textbooks",
    "Phoenix autocall: named after what happens to the trader's book",
    "Every exotic starts as a yield enhancer and ends as a hedge fund",
    "Structured product sold. Model risk opened.",
    "The payoff looked great on slide 4",
    "Knock-out forward: free leverage until the board finds out",
    "Range accrual: collecting daily coupons into a black hole",
    "Every bespoke structure is just a barrier option in a suit",

    # Vol surface & models
    "SABR model: wrong but industry standard",
    "Heston model: stochastic vol, deterministic losses",
    "Local vol model: smooth in theory, jumpy in practice",
    "SVI parameterization: fitting smiles, creating frowns",
    "Dupire local vol: elegant math, ugly hedges",
    "Jump diffusion: because continuous paths were too simple",
    "Rough vol: fractional Brownian motion, integer losses",
    "Vol surface calibration: fitting noise to noise",
    "Arbitrage-free surface: theoretically required, practically impossible",
    "No-arbitrage conditions: violated daily",
    "Black-Scholes: Nobel Prize for being elegantly wrong",
    "Normal distribution: a beautiful lie",
    "Fat tails: where your risk models go to die",
    "The model is perfect, reality is broken",
    "Vol surface: the map is not the territory",
    "Vol models: all wrong, some useful",
    "Calibrating the vol surface: fitting noise to noise",
    "The vol surface: 2D representation of 3D pain",
    "Vol Surface: a nice way to say B&S didn't know their a** from their elbows",
    "Black-Scholes: wrong but useful since 1973",
    "Sticky strike vs sticky delta: both wrong, pick your poison",
    "Smile today, cry tomorrow - the volatility smile story",
    "Stochastic vol: because constant vol was too optimistic",
    "Rough vol calibrates beautifully to the past. The future ignored the memo.",
    "SVI: arbitrage-free by construction, arbitrageable by reality",
    "The local vol surface is smooth. The hedges are not.",
    "Heston: two more parameters than Black-Scholes, twice the miscalibration",
    "Model risk: the risk your model is wrong, and it is",

    # Quant humor
    "Correlation is not causation, but it pays the bills",
    "Monte Carlo: because closed-form is too easy",
    "Machine learning: fitting noise faster",
    "Backtesting: the art of fitting curves to noise",
    "VaR model: wrong but required",
    "The backtest was magnificent",
    "Out-of-sample is where dreams go to die",
    "Confidence interval: confidently wrong",
    "Regression found a relationship. Reality disagreed.",
    "Correlation: friendship until stress arrives",
    "The model converged. The trade didn't.",
    "Statistically significant, economically irrelevant",
    "Assume normality, receive abnormal outcomes",
    "Stress testing: finding out you're already stressed",
    "The error term has entered the chat",
    "P&L is the final peer review",
    "The model is Cassandra: accurate, ignored, vindicated too late.",
    "Finite difference methods: finite accuracy, infinite runtime",
    "Nowcasting: being wrong in real-time",
    "Consensus forecast: where groupthink meets reality",
    "The quant built a perfect model. Nobody traded it.",
    "Sharpe ratio: measuring yesterday's luck with tomorrow's confidence",
    "Information ratio: the quant's way of saying 'trust me'",
    "Factor loading: attributing everything to something",
    "Every alpha decays. The question is whether you're still in it.",
    "PCA explained 87% of the variance. The 13% explained the loss.",

    # Desk culture
    "Traders: right 51% of the time, confident 100%",
    "Sales: promising what traders can't deliver since forever",
    "Quants: solving problems traders didn't know they had",
    "Risk: saying no in the most complicated way possible",
    "Compliance: the fun police",
    "Axe gone. Spread blown. Sales apologises later.",
    "The structurer is the only person who understands the trade. That's the problem.",
    "Quant research: 40 pages of math, one trading signal that doesn't work",
    "Sales credit: the original attribution problem",
    "Risk manager approved it. That's not reassuring.",
    "P&L is the only performance review that matters",
    "Every hero trade starts with 'this one's different'",
    "The spreadsheet works until it doesn't",

    # P&L
    "P&L: the universal language",
    "Green days build confidence, red days build character",
    "Unrealized P&L: Schrödinger's profit",
    "P&L attribution: creative accounting for traders",
    "Daily P&L: the only number that matters",
    "Year-end P&L: when bonuses are decided and friendships end",
    "Sell-side prestige gets you the interview, P&L gets you the offer",
    "PM longevity at a multistrat is measured in drawdown events survived",
    "Green P&L: skill. Red P&L: bad luck",
    "Profit is temporary, screenshots are eternal",
    "Marked to market, judged by management",
    "The spreadsheet says yes",
    "Attribution complete, mystery remains",
    "Today's alpha is tomorrow's beta",
    "The bonus is path dependent",
    "Performance review by mark-to-market",
    "The market audited my assumptions",
    "P&L is just a story until it settles",
    "The trade worked until money was involved",
    "The best trade was the one you didn't do",
    "Every drawdown starts small",
    "Conviction peaks at the top",
    "The market heard your stop",
    "FOMO is not a strategy",
    "Hope is not executable",
    "Risk management ruins great stories",
    "The market rewards humility eventually",

    # Hedge Fund / Multistrat / Pod shops
    "Multistrat: because losing money in multiple ways is more efficient",
    "Risk parity: equal risk of failure across all strategies",
    "Factor investing: yesterday's anomaly, today's crowded trade",
    "Stat arb: finding inefficiencies that don't exist",
    "Pairs trading: convergence eventually, just not before bankruptcy",
    "Mean reversion: works great until prices revert to zero",
    "Momentum: buying strength, selling weakness, wrong both ways",
    "Macro hedge fund: right thesis, wrong timing, right losses",
    "Long/short equity: long pain, short gains",
    "Hedge fund: taking 2 and 20 to underperform SPY",
    "Leverage: amplifying skill and stupidity in equal measure",
    "Drawdown: the only guaranteed return in investing",
    "Crisis alpha: alpha that only works during crises",
    "Crowded trade: when everyone's right until everyone's wrong",
    "Redemption notice: the market's way of saying 'timing'",
    "Pod shop risk limits: precise, non-negotiable, changed last Tuesday",
    "Shared services: everyone pays for the infrastructure, nobody knows what it costs",
    "Every trader is a volatility seller eventually",
    "Diversification: correlation goes to one when your AUM goes to zero",
    "Tail hedging: expensive insurance against the inevitable",
    "Quantitative strategies: backtesting on training data, blowing up on real data",
    "Portfolio optimization: maximizing correlations, minimizing returns",
    "Merger arb: arbitraging away your existence",
    "Rebalancing: selling winners, buying losers, systematically wrong",
    "Patience is a position",
    "Pod P&L is socialized, pod blame is not",
    "Stop-loss hit. PM on the line. Both at the same time.",
    "Multistrat: diversified risk, concentrated accountability",
    "The pod is flat. The PM is not.",
    "Gross exposure managed. Net exposure expressed its opinion anyway.",
    "Every pod starts with edge. Most end with explanation.",
    "Drawdown limit: the number you never thought you'd reach",
    "Capital allocation day: the best and worst day of the year",
    "The book was handed back cleaner than it came in. Nobody believed it.",
    "Risk decomp meeting: 45 minutes of Greeks, 0 minutes of insight",
    "Fundamental analysis: right direction, wrong decade",
    "Technical analysis: pretty charts, ugly P&L",
    "Discretionary trading: conviction until conviction is wrong",
    "Sector rotation: yesterday's winners, today's bag holders",

    # Macro / Event risk
    "Risk-off: when correlations go to one and liquidity goes to zero",
    "Event gamma: maximum risk, minimum reward",
    "Data release positioning: everyone's hedged, nobody's safe",
    "Economic data: the market's excuse to reprice",
    "Macro vol: can't predict it, can't hedge it, can't ignore it",
    "Event risk: what keeps vol traders employed",
    "Data surprise: the only constant in macro trading",
    "Macro trades are always early, which is indistinguishable from wrong",
    "The central bank surprised nobody and everyone repriced",
    "Fed day vol: bought expensive, sold cheaper",
    "Every macro thesis is correct at the annual horizon, useless at the daily",
    "The rate decision was in line. The statement wasn't. The vol was.",

    # Oil vol
    "Long oil vol, short world peace",
    "WTI: the asset class with commitment issues",
    "Every oil vol trader is a part-time geopolitical analyst",
    "Brent leads, WTI follows, everyone claims they knew",
    "The Middle East sneezes, oil vol catches pneumonia",
    "Oil traders don't predict wars, they just price them",
    "Crude oil: one molecule, infinite narratives",
    "Every short oil straddle comes with a free stress test",
    "The smile is steep because the world is unstable",
    "Oil skew: fear with a delivery point",
    "Long gamma into OPEC, short gamma into retirement",
    "In crude, tail events are just events",
    "Oil vol sellers rent risk from history",
    "Prompt vol: maximum uncertainty, minimum sleep",
    "OPEC meetings: volatility earnings season",
    "Every OPEC headline is both bullish and bearish",
    "OPEC surprises nobody except the market",
    "Inventory builds are bearish until they're bullish",
    "Cushing: the world's most important parking lot",
    "Fundamentals matter eventually. Headlines matter now",
    "The inventory report is just weekly P&L roulette",
    "Backwardation: getting paid to believe inventories are low",
    "Contango: paying storage rent with hope",
    "The front month is where confidence goes to die",
    "Physical traders know things. Paper traders know models",
    "Crack spreads: refining margins and trader sanity",
    "WTI traded below zero. Reality remains optional",
    "Negative oil prices: because finance wasn't weird enough",
    "April 2020: when storage became an asset class",
    "Selling oil vol is picking up dollars in front of a drone strike",
    "In crude markets, the tails have tails",
    "Crude options: where weather forecasts become risk factors",
    "Hurricanes are just volatility catalysts with names",
    "One refinery outage away from a new volatility regime",
    "Oil vol: all fun and games until the headline hits",
    "Black-Scholes never met a tanker blockade",
    "Every crude vol surface is a map of collective anxiety",
    "Commodity vol is macro with inventory constraints",
    "Prompt crude: maximum liquidity, minimum conviction",
    "The cure for high oil prices is high oil prices. The cure for low oil prices is unemployment",
    "Oil vol carry: collecting premium from future headlines",
    "Realized vol is what happened. Oil vol is what could happen",

    # Equity vol / SPX / 0DTE
    "Gold gamma: shiny metal, sharp losses",
    "Equity vol surface: skewed, kinked, and expensive",
    "SPX gamma: what you're short at the worst time",
    "0DTE options: because weekly expiry wasn't degenerate enough",
    "SPX put skew: permanently expensive, occasionally worth it",
    "Swaptions: options on swaps, regrets on both",
    "0DTE gamma: the retail product that repriced the vol surface",
    "SPX 0DTE: the casino asked for better odds",
    "Index skew: the crowd's collective memory of every tail event",
    "Single-stock vol: illiquid, mismarked, and somehow cheaper",
    "Vol of vol: the real underlying of every structured product",

    # Market wisdom
    "Markets can remain irrational longer than you can remain solvent",
    "The market is always right, except when it's wrong",
    "Liquidity is abundant until you need it",
    "Flash crash: when algorithms have a bad day",
    "Market maker: professional risk taker, amateur psychologist",
    "Liquidity? Don't know her",
    "Bid-ask spread: the market's way of saying 'no'",
    "You are never short vol; you are short catastrophe timing.",
    "Risk is just narrative until path dependency turns it mythic.",
    "The trader is Odysseus: surviving regimes, not forecasting them.",
    "A short vol book is Icarus with a carry stream.",
    "Smile steepening is the market whispering about disaster probability.",
    "Every book is a tragedy; pnl just decides the ending date.",
    "Markets don't break; they reveal they were always tragic.",
    "Correlations in crisis are the Fates cutting loose individuality.",
    "I trust the model. I fear the market.",
    "The model says maybe",
    "Risk approved it. That's concerning.",

    "The wings have already forgotten what the ATM hasn't learned yet",
    "The skew already knows what spot hasn't moved yet",
    "Vol surface remembers every crisis the ATM has since forgiven",
    "The put wing prices the world the call wing refuses to imagine",
    "The 10-delta strike is a memory of the last time everyone was wrong",
    "Implied vol peaks when realized vol is just getting started",
    "The smile bends toward the truth before the model accepts it",
    "The forward vol is mourning an event the spot market hasn't scheduled",
    "The wings carry the weight of every tail the distribution denied",
    "Skew steepens in the silence before anyone admits what they're hedging",
    "The term structure inverted before the economists had a word for it",
    "The 25-delta put remembers what the last calm regime chose to forget",
    "Vol of vol rises when certainty is still giving speeches",
    "The surface was already grieving when the model declared fair value",
    "The far strike prices a world the near strike still refuses to live in",

    # The baseline is different
    "EM: your tail risk is our Tuesday",
    "You call it armageddon. We call it just another day in the office.",
    "G10 calls it a regime change. EM calls it the third one this year.",
    "Developed markets discovered tail risk in 2008. We never lost it.",
    "EM vol surface has no memory because it never had the luxury of forgetting",
    "G10 traders hedge against crises. EM traders hedge between them.",
    "The EM smile was steep before 'geopolitical risk' was a slide deck category",
    "EM skew: not fear, just institutional memory",

    # Carry & the false calm
    "EM carry: three years of income, three days of losses",
    "The carry looked free until the central bank changed its mind at midnight",
    "EM carry unwind: the most predictable surprise in finance",
    "Everyone loves EM in the good times. The good times are never the point.",
    "The yield was real. The liquidity was a suggestion.",

    # Liquidity & execution
    "EM liquidity: there until you need it, gone before you ask",
    "Bid-offer in EM: a number and a prayer",
    "The axe was there yesterday. Today it's a different country.",
    "EM execution: the price you get is the price that was available",
    "Spread quoted. Spread doubled. Trade done at neither.",

    # Buy-side EM
    "EM PM: right on the macro, wrong on the timing, right on the losses",
    "The thesis was correct. The currency had other plans.",
    "In EM, the fundamentals are the story. The technicals are the actual trade.",

    "FX vol be like: I was calm for three months, did you miss me",
    "Gamma be like: you hedged this morning, cute",
    "EM carry be like: the yield is real, the exit is not",
    "Vanna be like: you fixed your delta and your vega, you're welcome",
    "The vol surface be like: I moved, figure out why",
    "Theta be like: weekends are on me",
    "Skew be like: I've been pricing this disaster since January",
    "EM FX be like: the central bank has entered the chat",
    "0DTE gamma be like: it's 3:45pm, are you sure about that position",
    "Realized vol be like: remember all those forecasts",
    "The barrier be like: you knew where I was",
    "OPEC be like: we have decided to surprise everyone equally",
    "Vol of vol be like: you thought regular vol was the problem",
    "The forward curve be like: I told you, you just didn't look",
    "Cross-gamma be like: both legs moved, neither hedge worked, good morning",
    "EM liquidity be like: I was here yesterday",
    "The smile be like: I'm not flat, I never said I was flat",
    "Drawdown be like: I started small, you had options",
    "Month-end vol be like: everyone marks, nobody agrees, P&L is a feeling",
    "The model be like: correct in expectation, useless in practice",
    
]



class QuoteGenerator:
    """
    Shuffle-deck based quote generator.
    No repeats until all quotes are exhausted.
    """

    def __init__(self, quotes: List[str]):
        self.quotes = quotes
        self._deck: List[str] = []
        self._recent: deque = deque(maxlen=max(1, len(quotes) // 4))

    def _refill_deck(self) -> None:
        self._deck = self.quotes[:]
        random.shuffle(self._deck)

    def _pop_from_deck(self) -> str:
        if not self._deck:
            self._refill_deck()
        # avoid recent repeats by skipping up to 10 candidates
        for _ in range(min(10, len(self._deck))):
            candidate = self._deck[-1]
            if candidate not in self._recent:
                self._deck.pop()
                self._recent.append(candidate)
                return candidate
            # move the unwanted candidate to a random earlier position
            self._deck.pop()
            self._deck.insert(random.randint(0, len(self._deck)), candidate)
        # give up avoiding recency, just pop
        candidate = self._deck.pop()
        self._recent.append(candidate)
        return candidate

    # ----------------------------
    # Core randomness
    # ----------------------------

    def get_random_quote(self, seed: Optional[int] = None) -> str:
        """Return a single fully random quote."""
        if seed is not None:
            return random.Random(seed).choice(self.quotes)
        return self._pop_from_deck()

    def get_random_quotes(self, n: int = 1, seed: Optional[int] = None) -> List[str]:
        """Return n random quotes (with replacement)."""
        if seed is not None:
            rng = random.Random(seed)
            return [rng.choice(self.quotes) for _ in range(n)]
        return [self._pop_from_deck() for _ in range(n)]

    def get_unique_random_quotes(self, n: int, seed: Optional[int] = None) -> List[str]:
        """Return n unique random quotes (without replacement)."""
        if seed is not None:
            rng = random.Random(seed)
            n = min(n, len(self.quotes))
            return rng.sample(self.quotes, n)
        results = []
        seen = set()
        while len(results) < min(n, len(self.quotes)):
            q = self._pop_from_deck()
            if q not in seen:
                seen.add(q)
                results.append(q)
        return results

    # ----------------------------
    # Filtered randomness (stateless)
    # ----------------------------

    def get_quote_by_keyword(self, keyword: str, seed: Optional[int] = None) -> str:
        """Return a random quote matching a keyword."""
        matches = [q for q in self.quotes if keyword.lower() in q.lower()]
        pool = matches if matches else self.quotes
        if seed is not None:
            return random.Random(seed).choice(pool)
        candidate = self._pop_from_deck()
        if keyword.lower() in candidate.lower():
            return candidate
        # fall back to random choice from matches
        return random.choice(pool)

    def get_quotes_by_keywords(self, keywords: List[str], n: int = 1, seed: Optional[int] = None) -> List[str]:
        """Return random quotes matching any keyword."""
        keywords = [k.lower() for k in keywords]
        matches = [q for q in self.quotes if any(k in q.lower() for k in keywords)]
        pool = matches if matches else self.quotes
        if seed is not None:
            rng = random.Random(seed)
            return [rng.choice(pool) for _ in range(n)]
        return [random.choice(pool) for _ in range(n)]

    # ----------------------------
    # Category-based randomness
    # ----------------------------

    def get_category_quote(self, category: str, seed: Optional[int] = None) -> str:
        """Return a random quote from a category (stateless filter)."""
        category_map = {
            "gamma": ["gamma"],
            "vega": ["vega"],
            "theta": ["theta", "time"],
            "delta": ["delta"],
            "vol": ["vol", "volatility", "smile", "skew"],
            "fx": ["fx", "eurusd", "carry"],
            "risk": ["risk", "hedge", "liquidity"],
            "exotic": ["exotic", "barrier", "tarf", "autocall"],
            "macro": ["cpi", "nfp", "fed", "ecb", "macro"],
        }
        keywords = category_map.get(category.lower(), [])
        matches = [q for q in self.quotes if any(k in q.lower() for k in keywords)] if keywords else []
        pool = matches if matches else self.quotes
        if seed is not None:
            return random.Random(seed).choice(pool)
        return random.choice(pool)

# ----------------------------
# Global instance + helpers
# ----------------------------

_generator = QuoteGenerator(TRADING_QUOTES)


def get_random_quote(seed: Optional[int] = None) -> str:
    return _generator.get_random_quote(seed)


def get_random_quotes(n: int = 1, seed: Optional[int] = None) -> List[str]:
    return _generator.get_random_quotes(n, seed)


def get_unique_random_quotes(n: int, seed: Optional[int] = None) -> List[str]:
    return _generator.get_unique_random_quotes(n, seed)


def get_quote_by_keyword(keyword: str, seed: Optional[int] = None) -> str:
    return _generator.get_quote_by_keyword(keyword, seed)


def get_category_quote(category: str, seed: Optional[int] = None) -> str:
    return _generator.get_category_quote(category, seed)
