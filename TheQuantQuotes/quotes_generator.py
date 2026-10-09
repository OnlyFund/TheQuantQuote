"""
Trading quotes generator for derivatives and volatility markets.
Investment bank options desk humor and wisdom.

Quotes are organised by category, so category lookups are exact rather than
keyword guesses. Unseeded calls draw from a shuffled deck (no repeats until
every quote has been shown); seeded calls are stateless and reproducible.
"""
from __future__ import annotations

import random
from collections import deque
from typing import Dict, Iterable, List, Optional, Sequence

QUOTES_BY_CATEGORY: Dict[str, List[str]] = {
    "gamma": [
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
        "Short vol smile - the lifespan of a Thanksgiving turkey",
        "Long gamma, short patience",
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
        "The gamma report was clean. The 4pm print wasn't.",
        "Gamma scalping: buying high, selling low, calling it alpha",
    ],
    "basis": [
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
    ],
    "vega": [
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
        "Vega flat on the matrix. Vega not flat on the actual surface.",
        "The vol surface doesn't care about your carry thesis",
    ],
    "theta": [
        "Theta decay: the only certainty in options",
        "Theta never sleeps, neither do option sellers",
        "Theta: slow violence",
        "Theta positive, life negative",
        "Weekend theta: the gift that keeps on giving",
        "Theta never misses payroll",
        "Theta: charging rent on borrowed hope",
        "Every option expires worthless eventually",
        "Theta positive, emotionally negative",
        "Theta paid for three months. Gamma collected in three days.",
        "The theta was real. The gamma event was realer.",
    ],
    "delta": [
        "Delta neutral, emotionally unstable",
        "Delta hedging: the art of controlled panic",
        "Delta hedging: because picking a direction is hard",
        "Your delta is showing",
        "Delta was never the problem",
        "Delta hedge first, ask questions later",
        "Flat delta, not flat emotions",
        "The market chose a direction for me",
        "Delta is temporary, slippage is forever",
        "Delta hedging: solving today's problem tomorrow",
        "Spot moved. There goes the hedge.",
        "Your directional view is showing",
        "Delta hedged to the model. Unhedged to what actually moved.",
    ],
    "fx": [
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
        "Risk reversal carry: collecting dimes in front of a steamroller that speaks central bank",
    ],
    "desk": [
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
        "Middle office knows where the bodies are buried",
        "That 'small position' has a funny way of growing",
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
        "The axe is never where the client needs it",
        "Axes are honest. Salespeople aren't.",
        "Flow that looks like flow isn't always flow",
        "The client hedged the wrong tenor because we showed them the liquid one",
        "Every axe has a story. Most of them end badly for the other side.",
        "Real flow moves the surface. Everything else is noise.",
        "The best axe is the one nobody knows you have",
        "Informed flow: the thing you suspect but can't prove until it's too late",
        "Client order in. Desk hedged. Surface moved. Coincidence.",
        "The axe gets lifted exactly when you needed it most",
        "The mid was indicative. The fill was not.",
        "Streaming price pulled the moment size was disclosed",
        "The market impact started before the order was sent",
        "The algo filled it. The trader explained it.",
        "Slippage: the spread between the backtest and reality",
        "The liquidity was there at 9am. By 9:01 it had seen the order.",
        "Best execution means different things to the client and the desk",
    ],
    "volatility": [
        "Implied vol is just expensive hope",
        "Realized vol: where predictions go to die",
        "Vol of vol: because one layer of complexity wasn't enough",
        "Vol risk premium: gap between fear and reality",
        "Vol mean reversion: eventually, maybe, hopefully",
        "Realized-implied spread: the trade that never works",
        "Long vol: right eventually, broke immediately",
        "Short vol: profitable until it's catastrophic",
        "Vol regime change: when your model breaks",
        "Forward vol: today's uncertainty about tomorrow's uncertainty",
        "Short vol in a low-vol regime: picking up nickels, not dimes",
        "Vol carry works until the event everyone forgot about",
        "Selling vol: great strategy, terrible timing, every time",
        "Vol carry: you're not collecting premium, you're selling the right to be bailed out",
        "Long vol in a carry regime is just paying tuition",
        "Selling straddles for yield: the strategy that works until the portfolio doesn't",
        "The vol risk premium is real. So is the drawdown when it unwinds.",
        "Every vol regime looks obvious in hindsight and invisible in real time",
        "The variance swap knew it was a crisis before the equity desk did",
        "Short vol is a strategy. Short vol forever is a character flaw.",
        "Vol targeting: systematically buying high and selling low with a mandate",
        "The correlation break always happens inside the vol strategy that assumed it wouldn't",
        "Selling puts for income: a bond strategy with unlimited downside and limited self-awareness",
        "Every structured vol strategy has a hidden short gamma somewhere",
    ],
    "skew": [
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
    ],
    "greeks": [
        "The only Greek that matters is the P&L",
        "Correlation goes to one when you need it least",
        "One more Greek should fix this",
        "There is always another Greek",
        "The Greeks send their regards",
        "Greek-neutral, problem-positive",
        "The hedge has hedges now",
        "Greeks explained everything except the losses",
        "Cross-greeks: collaborative suffering",
        "Higher-order Greeks, lower-order judgment",
        "Know your Greeks, lose money anyway",
        "The Greeks always had a thing with tragedies",
        "First-order Greeks: what you hedge. Second-order Greeks: what kills you",
        "Greeks report: 47 pages of numbers, zero insight",
        "Greeks neutral: theoretically possible, practically impossible",
        "Greeks dashboard: red everywhere, explanations nowhere",
        "Managing Greeks: like juggling chainsaws, blindfolded",
        "Greeks in crisis: all positive, portfolio still negative",
        "Greeks neutralised. P&L not consulted.",
        "The cross-gamma wasn't in the risk report because nobody thought to ask",
        "The rho was irrelevant until rates moved 200bps in six weeks",
    ],
    "higher_order": [
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
        "The vanna exposure was in the footnotes. The loss was on the blotter.",
        "Charm at month-end: the Greek that turns a flat book into an active one",
        "Volga is just the market charging you for being wrong about vol of vol",
    ],
    "barriers": [
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
        "The knock-out was 3% away. It felt like it wasn't.",
    ],
    "exotics": [
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
        "The term sheet was 60 pages. The risk was on page 61.",
        "Autocall pricing: giving away vol to sell a yield that sounds like a bond",
        "The worst-of basket correlation was set to 0.7. It realized at 0.95.",
        "Structured product margin: front-loaded for the desk, back-loaded for the client",
        "Every autocall sold is a variance swap bought by someone else",
        "TARF: the product where the client wins small and loses big, elegantly structured",
    ],
    "models": [
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
        "Fat tails: where your risk models go to die",
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
    ],
    "quant": [
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
        "The strategy worked in the backtest because it front-ran itself",
    ],
    "rates": [
        "Swaptions: options on swaps, regrets on both",
        "Swaption vol: where rates uncertainty meets optionality and both lose",
        "The rates vol surface repriced overnight. The delta hedge was daily.",
        "Receivers vs payers skew: the market's opinion on where the central bank panics",
        "Swaption gamma: interest rate risk that arrives without warning",
        "Bermudan callable: the client's right to ruin your hedge at the worst moment",
        "CMS spread options: two rates, one surface, infinite ways to miscalibrate",
        "The vol surface said rates were rangebound. The FOMC didn't get the memo.",
        "Swap spread vol: basis risk with a duration overlay",
    ],
    "correlation": [
        "Dispersion trades: long single-name vol, short index vol, short sanity",
        "Dispersion trade: short the index knowing the single names will humiliate you individually",
        "Correlation is the trade that looks diversified until it isn't",
        "Long dispersion: right on the structure, wrong on the timing, always",
        "The index moved less than the components. Correlation trading 101.",
        "Correlation swaps: pricing a relationship the market will definitely violate",
        "Every dispersion desk has a story that starts with 'implied correlation was too high'",
        "Single-stock vol rich, index vol cheap, correlation trade obvious, P&L not",
    ],
    "culture": [
        "P&L is the only performance review that matters",
        "Every hero trade starts with 'this one's different'",
        "The spreadsheet works until it doesn't",
        "The structurer is the only person who understands the trade. That's the problem.",
        "Quant research: 40 pages of math, one trading signal that doesn't work",
        "Sales credit: the original attribution problem",
        "Risk manager approved it. That's not reassuring.",
        "Quants: solving problems traders didn't know they had",
        "Risk: saying no in the most complicated way possible",
        "Risk management ruins great stories",
    ],
    "pnl": [
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
        "Attribution complete, mystery remains",
        "The bonus is path dependent",
        "Performance review by mark-to-market",
        "The market audited my assumptions",
        "P&L is just a story until it settles",
        "The best trade was the one you didn't do",
        "Every drawdown starts small",
        "Conviction peaks at the top",
        "The market heard your stop",
        "FOMO is not a strategy",
        "Hope is not executable",
    ],
    "multistrat": [
        "Multistrat: because losing money in multiple ways is more efficient",
        "Risk parity: equal risk of failure across all strategies",
        "Factor investing: yesterday's anomaly, today's crowded trade",
        "Stat arb: finding inefficiencies that don't exist",
        "Macro hedge fund: right thesis, wrong timing, right losses",
        "Long/short equity: long pain, short gains",
        "Hedge fund: taking 2 and 20 to underperform SPY",
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
        "Discretionary trading: conviction until conviction is wrong",
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
        "Multistrat PMs don't blow up. Their capital just gets reallocated.",
        "The pod had edge. The crowding didn't care.",
        "Pod sizing: risk limits set by someone who's never held the position",
        "Every alpha stream is uncorrelated until redemption season",
        "The book looked flat to risk. It wasn't flat to the market.",
        "Gross exposure cut. Net exposure expressed itself anyway.",
        "The stop-loss was the right call. The PM made it three weeks late.",
        "Multistrat: where strategies come to get correlated",
        "The allocation committee liked the Sharpe. The drawdown found the skew.",
        "Every pod is market neutral until the market moves",
        "Portfolio construction meeting: where good trades go to get diluted",
        "Risk decomp showed no concentration. The unwind disagreed.",
        "The PM left. The positions stayed. The risk didn't know the difference.",
        "Capacity constrained at $200m. Running $800m. Vintage 2024.",
    ],
    "macro": [
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
    ],
    "oil": [
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
    ],
    "equity_vol": [
        "Gold gamma: shiny metal, sharp losses",
        "Equity vol surface: skewed, kinked, and expensive",
        "SPX gamma: what you're short at the worst time",
        "0DTE options: because weekly expiry wasn't degenerate enough",
        "SPX put skew: permanently expensive, occasionally worth it",
        "0DTE gamma: the retail product that repriced the vol surface",
        "SPX 0DTE: the casino asked for better odds",
        "Index skew: the crowd's collective memory of every tail event",
        "Single-stock vol: illiquid, mismarked, and somehow cheaper",
        "Vol of vol: the real underlying of every structured product",
    ],
    "wisdom": [
        "Liquidity is abundant until you need it",
        "You are never short vol; you are short catastrophe timing.",
        "Risk is just narrative until path dependency turns it mythic.",
        "The trader is Odysseus: surviving regimes, not forecasting them.",
        "A short vol book is Icarus with a carry stream.",
        "Smile steepening is the market whispering about disaster probability.",
        "Every book is a tragedy; pnl just decides the ending date.",
        "Markets don't break; they reveal they were always tragic.",
        "Correlations in crisis are the Fates cutting loose individuality.",
        "I trust the model. I fear the market.",
        "Risk approved it. That's concerning.",
    ],
    "surface_poetry": [
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
    ],
    "desk_poetic": [
        "The hedge was perfect. The world wasn't.",
        "Skew doesn't lie. Traders do.",
        "Every vol surface is an argument about the future nobody wins.",
        "The smile was there before you were.",
        "Gamma found the position before risk did.",
        "The book was flat. The market disagreed personally.",
        "Vol sold off. Someone knew.",
        "The barrier held until it had an audience.",
        "You don't lose to the market. You lose to the version of yourself that put the trade on.",
        "The surface moved. The model explained it afterwards.",
    ],
    "em": [
        "EM: your tail risk is our Tuesday",
        "You call it armageddon. We call it just another day in the office.",
        "G10 calls it a regime change. EM calls it the third one this year.",
        "Developed markets discovered tail risk in 2008. We never lost it.",
        "EM vol surface has no memory because it never had the luxury of forgetting",
        "G10 traders hedge against crises. EM traders hedge between them.",
        "The EM smile was steep before 'geopolitical risk' was a slide deck category",
        "EM skew: not fear, just institutional memory",
        "EM carry: three years of income, three days of losses",
        "The carry looked free until the central bank changed its mind at midnight",
        "EM carry unwind: the most predictable surprise in finance",
        "Everyone loves EM in the good times. The good times are never the point.",
        "The yield was real. The liquidity was a suggestion.",
        "EM liquidity: there until you need it, gone before you ask",
        "Bid-offer in EM: a number and a prayer",
        "The axe was there yesterday. Today it's a different country.",
        "EM execution: the price you get is the price that was available",
        "Spread quoted. Spread doubled. Trade done at neither.",
        "EM PM: right on the macro, wrong on the timing, right on the losses",
        "The thesis was correct. The currency had other plans.",
        "In EM, the fundamentals are the story. The technicals are the actual trade.",
    ],
    "be_like": [
        "FX vol be like: I was calm for three months, did you miss me",
        "Gamma be like: you hedged this morning, cute",
        "EM carry be like: the yield is real, the exit is not",
        "Vanna be like: you fixed your delta and your vega, you're welcome",
        "Theta be like: weekends are on me",
        "Skew be like: I've been pricing this disaster since January",
        "EM FX be like: the central bank has entered the chat",
        "0DTE gamma be like: it's 3:45pm, are you sure about that position",
        "The barrier be like: you knew where I was",
        "OPEC be like: we have decided to surprise everyone equally",
        "Cross-gamma be like: both legs moved, neither hedge worked, good morning",
        "EM liquidity be like: I was here yesterday",
        "Drawdown be like: I started small, you had options",
        "Month-end vol be like: everyone marks, nobody agrees, P&L is a feeling",
    ],
    "vol_surface": [
        "Ask three desks for the 1y 10-delta put and you'll get four marks and one resignation",
        "If your surface has no kinks, you haven't looked at it since Tuesday",
        "A vol surface is a group chat where every strike thinks it's the adult",
        "Interpolate between liquid points and you have a mark; extrapolate past them and you have a confession",
        "Half the surface trades. The other half is held up by SVI and good intentions",
        "Show me your far wings and I'll tell you what scared you in 2020",
        "We smoothed the surface so well it stopped telling us anything",
        "Before you call the wings rich, try selling them in size",
        "Sticky strike or sticky delta? Ask after the move and everyone remembers choosing correctly",
        "Nobody gets fired for marking the wings wide. They just never get filled",
    ],
    "regimes": [
        "Regimes don't announce themselves; they send the calendar invite after the meeting",
        "Every regime-switching model has detected the previous regime perfectly",
        "Once a regime has a name, you've already paid its tuition",
        "Low vol isn't calm. It's the market holding its breath with excellent posture",
        "Three quiet months is all it takes for a desk to rebrand complacency as process",
        "Vol doesn't trend. It waits, sprints, then pretends it was walking the whole time",
        "If you need a second chart to prove the regime changed, it hasn't",
        "Mean reversion is a promise paid in a currency you may no longer hold",
        "Every risk model is fitted to a regime that is, statistically, about to end",
        "Nothing ages a vol trader faster than a regime that changes on a Friday afternoon",
    ],
    "em_regimes": [
        "In G10 an intervention is a headline. In EM it's a Wednesday, sometimes a Thursday too",
        "The best EM vol model is a phone number at the central bank that still answers",
        "EM implieds aren't high; they're priced for a world where weekends exist",
        "Every managed float is a short straddle with a press office",
        "Sell EM vol in a quiet patch and you're not collecting premium, you're renting a government's patience",
        "In EM the term structure inverts on rumour and normalises on denial",
        "In an EM election year the forward vol has the date circled before the candidates have written their speeches",
        "Capital controls turn a vol surface into a museum exhibit: look all you like, but don't touch",
        "EM vol regimes last exactly as long as the finance minister",
        "Onshore and offshore surfaces agree on everything except price, direction and whether you're allowed to trade",
        "If the EM smile looks flat, check whether anyone is actually quoting it",
        "Realised vol on a peg is zero right up until it's the whole year",
    ],
}

# Friendly alternative names for categories (including the old keyword-map names).
CATEGORY_ALIASES: Dict[str, str] = {
    "vol": "volatility",
    "fx_vol": "fx",
    "risk": "desk",
    "flow": "desk",
    "exotic": "exotics",
    "structured": "exotics",
    "barrier": "barriers",
    "vanna": "higher_order",
    "volga": "higher_order",
    "charm": "higher_order",
    "model": "models",
    "swaptions": "rates",
    "dispersion": "correlation",
    "hf": "multistrat",
    "pods": "multistrat",
    "crude": "oil",
    "equity": "equity_vol",
    "spx": "equity_vol",
    "poetic": "wisdom",
    "surface": "vol_surface",
    "regime": "regimes",
    "em_vol": "em_regimes",
}


def _dedupe(quotes: Iterable[str]) -> List[str]:
    """Remove exact duplicates while keeping the original order."""
    return list(dict.fromkeys(quotes))


TRADING_QUOTES: List[str] = _dedupe(
    q for quotes in QUOTES_BY_CATEGORY.values() for q in quotes
)


class QuoteGenerator:
    """
    Shuffle-deck quote generator.

    Unseeded calls share one deck: no quote repeats until every quote has been
    shown, and quotes shown recently are kept off the top of the next deck.
    Seeded calls are stateless and reproducible; they never touch the deck.
    """

    def __init__(
        self,
        quotes_by_category: Dict[str, Sequence[str]],
        aliases: Optional[Dict[str, str]] = None,
        rng: Optional[random.Random] = None,
    ):
        self._by_category: Dict[str, List[str]] = {
            name.lower(): _dedupe(quotes) for name, quotes in quotes_by_category.items()
        }
        self.quotes: List[str] = _dedupe(
            q for quotes in self._by_category.values() for q in quotes
        )
        if not self.quotes:
            raise ValueError("QuoteGenerator needs at least one quote")
        self._aliases = {k.lower(): v.lower() for k, v in (aliases or {}).items()}
        self._rng = rng or random.Random()
        self._deck: List[str] = []
        self._recent: deque = deque(maxlen=max(1, len(self.quotes) // 4))

    @property
    def categories(self) -> List[str]:
        return sorted(self._by_category)

    # ----------------------------
    # Internals
    # ----------------------------

    def _refill_deck(self) -> None:
        deck = self.quotes[:]
        self._rng.shuffle(deck)
        # Cards are drawn from the end, so put recently shown quotes at the
        # front: they come up last. sort() is stable, so the shuffle survives.
        recent = set(self._recent)
        deck.sort(key=lambda q: q not in recent)
        self._deck = deck

    def _draw(self) -> str:
        """Draw the next quote from the shared deck."""
        if not self._deck:
            self._refill_deck()
        quote = self._deck.pop()
        self._recent.append(quote)
        return quote

    def _draw_from(self, pool: Sequence[str]) -> str:
        """Draw from a subset, preferring quotes not shown recently."""
        recent = set(self._recent)
        fresh = [q for q in pool if q not in recent]
        quote = self._rng.choice(fresh or list(pool))
        if quote in self._deck:
            self._deck.remove(quote)  # don't show it again from the main deck
        self._recent.append(quote)
        return quote

    def _pick(self, pool: Sequence[str], seed: Optional[int]) -> str:
        if seed is not None:
            return random.Random(seed).choice(pool)
        return self._draw_from(pool)

    def _matches(self, keywords: Iterable[str]) -> List[str]:
        kws = [k.lower().strip() for k in keywords if k and k.strip()]
        return [q for q in self.quotes if any(k in q.lower() for k in kws)]

    def _category_pool(self, category: str) -> List[str]:
        key = category.lower().strip()
        key = self._aliases.get(key, key)
        if key not in self._by_category:
            raise ValueError(
                f"Unknown category {category!r}. Choose from: {', '.join(self.categories)}"
            )
        return self._by_category[key]

    # ----------------------------
    # Core randomness
    # ----------------------------

    def get_random_quote(self, seed: Optional[int] = None) -> str:
        """Return one random quote."""
        if seed is not None:
            return random.Random(seed).choice(self.quotes)
        return self._draw()

    def get_random_quotes(self, n: int = 1, seed: Optional[int] = None) -> List[str]:
        """
        Return n random quotes.

        Unseeded, these come off the deck, so repeats only happen once n runs
        past the size of the collection. Seeded, they are drawn with replacement.
        """
        if n < 0:
            raise ValueError("n must be non-negative")
        if seed is not None:
            rng = random.Random(seed)
            return [rng.choice(self.quotes) for _ in range(n)]
        return [self._draw() for _ in range(n)]

    def get_unique_random_quotes(self, n: int, seed: Optional[int] = None) -> List[str]:
        """Return up to n distinct quotes (capped at the collection size)."""
        n = min(max(n, 0), len(self.quotes))
        if seed is not None:
            return random.Random(seed).sample(self.quotes, n)
        results: List[str] = []
        seen = set()
        # Every deck holds each distinct quote once, so this ends within two decks.
        while len(results) < n:
            quote = self._draw()
            if quote not in seen:
                seen.add(quote)
                results.append(quote)
        return results

    # ----------------------------
    # Filtered randomness
    # ----------------------------

    def get_quote_by_keyword(self, keyword: str, seed: Optional[int] = None) -> str:
        """Return a random quote containing the keyword (any quote if none match)."""
        pool = self._matches([keyword]) or self.quotes
        return self._pick(pool, seed)

    def get_quotes_by_keywords(
        self, keywords: List[str], n: int = 1, seed: Optional[int] = None
    ) -> List[str]:
        """Return n random quotes containing any keyword (any quotes if none match)."""
        if n < 0:
            raise ValueError("n must be non-negative")
        pool = self._matches(keywords) or self.quotes
        if seed is not None:
            rng = random.Random(seed)
            return [rng.choice(pool) for _ in range(n)]
        return [self._draw_from(pool) for _ in range(n)]

    def get_category_quote(self, category: str, seed: Optional[int] = None) -> str:
        """Return a random quote from a category. Raises ValueError if unknown."""
        return self._pick(self._category_pool(category), seed)

    def get_category_quotes(
        self, category: str, n: int = 1, seed: Optional[int] = None
    ) -> List[str]:
        """Return n random quotes from a category. Raises ValueError if unknown."""
        if n < 0:
            raise ValueError("n must be non-negative")
        pool = self._category_pool(category)
        if seed is not None:
            rng = random.Random(seed)
            return [rng.choice(pool) for _ in range(n)]
        return [self._draw_from(pool) for _ in range(n)]


# ----------------------------
# Global instance + helpers
# ----------------------------

_generator = QuoteGenerator(QUOTES_BY_CATEGORY, aliases=CATEGORY_ALIASES)


def list_categories() -> List[str]:
    return _generator.categories


def get_random_quote(seed: Optional[int] = None) -> str:
    return _generator.get_random_quote(seed)


def get_random_quotes(n: int = 1, seed: Optional[int] = None) -> List[str]:
    return _generator.get_random_quotes(n, seed)


def get_unique_random_quotes(n: int, seed: Optional[int] = None) -> List[str]:
    return _generator.get_unique_random_quotes(n, seed)


def get_quote_by_keyword(keyword: str, seed: Optional[int] = None) -> str:
    return _generator.get_quote_by_keyword(keyword, seed)


def get_quotes_by_keywords(
    keywords: List[str], n: int = 1, seed: Optional[int] = None
) -> List[str]:
    return _generator.get_quotes_by_keywords(keywords, n, seed)


def get_category_quote(category: str, seed: Optional[int] = None) -> str:
    return _generator.get_category_quote(category, seed)


def get_category_quotes(category: str, n: int = 1, seed: Optional[int] = None) -> List[str]:
    return _generator.get_category_quotes(category, n, seed)


__all__ = [
    "QUOTES_BY_CATEGORY",
    "CATEGORY_ALIASES",
    "TRADING_QUOTES",
    "QuoteGenerator",
    "list_categories",
    "get_random_quote",
    "get_random_quotes",
    "get_unique_random_quotes",
    "get_quote_by_keyword",
    "get_quotes_by_keywords",
    "get_category_quote",
    "get_category_quotes",
]


if __name__ == "__main__":
    for name in list_categories():
        print(f"[{name}] {get_category_quote(name)}")
