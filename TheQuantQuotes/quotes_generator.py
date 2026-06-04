"""
Trading quotes generator for derivatives and volatility markets.
Investment bank options desk humor and wisdom.
"""
import random
from typing import List
from collections import deque

# Collection of trading wisdom and options desk humor
TRADING_QUOTES = [
    # Gamma quotes
    "Gamma kills, but theta heals",
    "Short gamma, long trauma",
    "Theta pays the rent, Gamma takes the house",
    "Friends don't let friends sell naked gamma",
    "Gamma: the silent portfolio killer",
    "In gamma we trust, in delta we adjust",
    "Gamma scalping: because sleep is overrated",
    "Vol Risk Premium: good luck capturing that...",
    "Long gamma, short sanity",
    "A 1Δ option on the day of expiry : the stuff traders' nightmares are made of",
    "Stoch-Local Vol is not a model choice, it's a commitment issue",
    "Every time that an axe gets filled, a sales trader gets his wings",
    "USDJPY drops 1% - maybe something, probably nothing",
    'Zero: the only true answer to the question "How low vols can go"',
    'Short vol smile - the lifespan of a Thanksgiving turkey',
    'Long gamma, short patience',
    
    "Vega hurts when you least expect it",
    "Long vega, short nerves",
    "Vega Hurts, Gamma Kills",
    "When vega spikes, portfolios dive",
    "Vega is a cruel mistress",
    "Vega P&L: the rollercoaster nobody asked for",
    "Vega convexity: expensive and misunderstood",

    # Theta quotes
    "Theta decay: the only certainty in options",
    "Time is money, theta is proof",
    "Theta never sleeps, neither do option sellers",
    "Theta: slowly bleeding your premium since 1973",
    "Theta positive, life negative",
    "Weekend theta: the gift that keeps on giving",

    # Delta quotes
    "Delta neutral, emotionally unstable",
    "Delta neutra, emotionally drained",
    "Delta hedging: the art of controlled panic",
    "Stay delta neutral, stay sane",
    "Delta one, problems none",
    "Delta hedging: because picking a direction is hard",
    "Your delta is showing",

    # FX Vol specific
    "FX vol: where central banks ruin your day",
    "EURUSD vol: boring until it's not",
    "Cable vol: Brexit's eternal gift",
    "EM FX vol: because you hate stability",
    "G10 vol: low and slow until it explodes",
    "Spot moves 5%, vol moves 50%, desk moves to new jobs",
    "FX vol smile: because markets aren't normal",
    "Carry trade: free money until it's not",
    "FX options: where 25 delta means something",
    "Butterfly spread: for when you're wrong about everything",
    "Vol surface: flat in theory, bumpy in practice",

    # Options desk humor
    "Marked my book, marked my soul",
    "P&L explain: creative writing for traders",
    "Risk limits: suggestions, not rules",
    "Model says buy, gut says sell, compliance says no",
    "Hedged my Greeks, forgot my sanity",
    "Bid-offer spread: how wide can we go?",
    "Month-end: when everyone pretends to care about risk",
    "Unwind that position? But it's my favorite loser",

    # Volatility quotes
    "Volatility is the only free lunch in finance",
    "Low vol kills, high vol thrills",
    "Implied vol is just expensive hope",
    "Realized vol: where predictions go to die",
    "Volatility: can't live with it, can't trade without it",
    "Vol of vol: because one layer of complexity wasn't enough",
    "Sticky strike, sticky delta, sticky P&L",
    "Vol clustering: bad news travels in packs",
    "Historical vol: useless but we calculate it anyway",

    # Risk Reversal quotes
    "Strangles: because picking a direction is hard",
    "Skew happens",
    "Skew trade: right direction, wrong timing, no P&L",
    "If you like our 25-delta RR, you will LOVE our 10-delta",


    # General derivatives wisdom
    "Options: limited risk, unlimited regret",
    "Derivatives: weapons of mass financial destruction",
    "The only Greek that matters is the P&L",
    "Hedge early, hedge often, still lose money",
    "Convexity: expensive insurance you hope to never use",
    "Correlation goes to one when you need it least",
    "In volatility trading, the house always wins... eventually",
    "Mark-to-market: where dreams become nightmares",
    "Greeks are theoretical, losses are real",
    "Smile today, cry tomorrow - the volatility smile story",
    "Exotic options: because vanilla is too profitable",

    # Butterfly quotes
    "Butterflies: beautiful in nature, painful in portfolios",
    "Long butterfly, short sanity",
    "Butterfly spreads: because you hate money",
    "Butterfly P&L: death by a thousand cuts",

    # Straddle/Strangle quotes
    "Long straddle: betting on chaos",
    "Short straddle: selling insurance on the Titanic",
    "Strangles: for when you're wrong both ways",
    "ATM straddle: maximum pain, minimum gain",

    # Vol surface quotes
    "The vol surface is flat, said no trader ever",
    "Term structure inversion: nature's warning sign",
    "Vol surface arbitrage: free money in theory",
    "Calibrating the vol surface: fitting noise to noise",
    "Vol Surface: a nice way to say B&S didn't know their a** from their elbows",
    "Sticky strike vs sticky delta: both wrong, pick your poison",
    "Vol surface modeling: fixing Black-Scholes one Greek at a time",
    "Vol surface arbitrage: exploiting Black-Scholes' ignorance",
    "Black-Scholes: Nobel Prize for being elegantly wrong",

    # Trading psychology
    "Hedge your Greeks, not your emotions",
    "The best hedge is a good night's sleep",
    "Risk management: because YOLO doesn't work in derivatives",
    "Stress testing: finding out you're already stressed",
    "Backtesting: the art of fitting curves to noise",
    "VaR model: wrong but required",

    # Market wisdom
    "Markets can remain irrational longer than you can remain solvent",
    "The market is always right, except when it's wrong",
    "Liquidity is abundant until you need it",
    "Bid-ask spread: the market's way of saying 'no'",
    "Flash crash: when algorithms have a bad day",
    "Market maker: professional risk taker, amateur psychologist",
    "Liquidity? Don't know her",

    # Barrier options
    "Barrier options: because vanilla is too boring",
    "Knock-in, knock-out, knock yourself out",
    "Barrier breach at 2:59pm? Classic",
    "One-touch option: touched once, regretted forever",
    "Don't care about the terminal distribution, give me the whole damn path",

    # Quant humor
    "Black-Scholes: wrong but useful since 1973",
    "Normal distribution: a beautiful lie",
    "Fat tails: where your risk models go to die",
    "Correlation is not causation, but it pays the bills",
    "The model is perfect, reality is broken",
    "Monte Carlo: because closed-form is too easy",
    "Stochastic vol: because constant vol was too simple",

    # Desk culture
    "Traders: right 51% of the time, confident 100%",
    "Sales: promising what traders can't deliver since forever",
    "Quants: solving problems traders didn't know they had",
    "Risk: saying no in the most complicated way possible",
    "IT: turning it off and on again, but for millions",
    "Compliance: the fun police",

    # P&L wisdom
    "Green P&L: skill. Red P&L: bad luck",
    "Unrealized P&L: Schrödinger's profit",
    "P&L attribution: creative accounting for traders",
    "Daily P&L: the only number that matters",
    "Year-end P&L: when bonuses are decided and friendships end",

    # Vanna quotes
    "Vanna: when your delta hedge needs a hedge",
    "Vanna risk: gamma's evil twin",
    "Long vanna, short explanations to risk managers",
    "Vanna P&L: the Greek nobody asked for",
    "Vanna hedging: because first-order Greeks were too easy",
    "Vanna exposure: when spot and vol move together, you lose twice",
    "Vanna/Volga - never worths it, always painful",
    "Vanna/Volga Greeks: calculated to the fifth decimal, wrong to the first",

    # Volga/Vomma quotes
    "Volga: gamma for vol traders",
    "Volga positive until it's not",
    "Vomma: the Greek that breaks your vol models",
    "Volga hedging: theoretical in textbooks, impossible in practice",
    "Short volga, short sleep",
    "Short Cross-Gamma: because shock therapy isn't working anymore",
    "Volga convexity: expensive and misunderstood",

    # Charm quotes
    "Charm: theta's derivative, trader's nightmare",
    "Charm decay: when your delta hedge expires",
    "Charm risk: because regular theta wasn't painful enough",
    "Monitoring charm at month-end: a special kind of masochism",


    # Color quotes
    "Color: gamma's gamma, sanity's enemy",
    "Color risk: third-order problems require first-order solutions",
    "Hedging color? Just close the position",
    "Color P&L explain: 'It's complicated'",

    # Ultima quotes
    "Ultima: because vomma wasn't enough",
    "Ultima risk: when you're three derivatives deep and lost",
    "Calculating ultima: the quant's flex",

    # Speed quotes
    "Speed: when gamma moves too fast",
    "Speed risk: gamma's acceleration, trader's deceleration",

    # Zomma quotes
    "Zomma: the Greek that sounds made up",
    "Zomma hedging: theoretical exercise, practical nightmare",

    # General high-order Greeks
    "Second-order Greeks: where models meet reality and lose",
    "Third-order Greeks: because we hate simplicity",
    "Cross-Greeks: when one dimension of pain isn't enough",
    "Higher-order Greeks: job security for quants",
    "Greeks beyond delta: diminishing returns, increasing confusion",
    "Hedging second-order Greeks: expensive and futile",
    "High-order Greeks: the difference between theory and practice",
    "Managing cross-gamma: a fool's errand",

    # ========================================================================
    # GREEKS AS A CULTURE
    # ========================================================================

    "Greeks: named by mathematicians, feared by traders",
    "The Greeks always had a thing with tragedies",
    "Learning Greeks: easy. Understanding Greeks: impossible. Hedging Greeks: futile",
    "The Greeks: a tragedy in five acts (delta, gamma, vega, theta, rho)",
    "Greeks ladder: delta, gamma, vanna, volga, and regret",
    "First-order Greeks: what you hedge. Second-order Greeks: what kills you",
    "Greeks report: 47 pages of numbers, zero insight",
    "Greek letters: because English wasn't confusing enough",
    "Know your Greeks, lose money anyway",
    "Greeks neutral: theoretically possible, practically impossible",
    "The Greeks: ancient wisdom, modern pain",
    "Greeks dashboard: red everywhere, explanations nowhere",
    "Managing Greeks: like juggling chainsaws, blindfolded",
    "Greeks P&L: when math meets Murphy's law",
    "Cross-Greeks: because single-variable risk was too simple",
    "Greeks in crisis: all positive, portfolio still negative",
    "Explaining Greeks to management: lost in translation",
    "Greeks hedging: rearranging deck chairs on the Titanic",
    "The Greek alphabet: 24 letters, infinite ways to lose money",
    "Greeks convergence: when all your hedges fail simultaneously",
    "Dynamic Greeks: because static Greeks were too predictable",

    "Risk-off: when correlations go to one and liquidity goes to zero",
    "Event gamma: maximum risk, minimum reward",
    "Data release positioning: everyone's hedged, nobody's safe",
    "Nowcasting: being wrong in real-time",
    "Economic data: the market's excuse to reprice",
    "Macro vol: can't predict it, can't hedge it, can't ignore it",
    "Event risk: what keeps vol traders employed",
    "Data surprise: the only constant in macro trading",
    "Consensus forecast: where groupthink meets reality",

    # ========================================================================
    # EXOTIC OPTIONS & STRUCTURED PRODUCTS
    # ========================================================================

    # Path-dependent exotics
    "Asian options: because one fixing wasn't painful enough",
    "Lookback options: hindsight is 20/20, pricing is impossible",
    "Parisian options: barrier breach with a waiting period, because why not",
    "Asian tail risk: averaging doesn't eliminate, just delays pain",

    # Barrier exotics
    "Double barrier: twice the risk, half the premium",
    "Reverse knock-out: because regular barriers were boring",
    "Window barriers: barrier only matters sometimes, pricing matters always",
    "Partial barriers: because full barriers were too honest",
    "American barriers: can breach anytime, will breach at worst time",
    "Barrier monitoring: continuous in theory, discrete in practice, painful always",
    "Rebate barriers: consolation prize for losers",

    # Multi-asset exotics
    "Basket options: diversification in theory, correlation in practice",
    "Rainbow options: colorful name, monochrome P&L",
    "Best-of options: best of nothing is still nothing",
    "Worst-of options: because someone hates you",
    "Quanto options: FX risk you didn't know you had",
    "Correlation swaps: betting on relationships that don't exist",
    "Dispersion trades: long single-name vol, short index vol, short sanity",

    # Volatility exotics
    "Variance swaps: pure vol exposure, impure P&L",
    "Volatility swaps: variance swap's complicated cousin",
    "Corridor variance: vol only counts sometimes",
    "Conditional variance: because regular variance wasn't fun enough",
    "Gamma swaps: third-order pain",
    "Vol swaps: convexity you can't hedge",
    "Variance dispersion: when correlation kills",

    # Target redemption & accumulators
    "TARFs: target redemption, actual destruction",
    "Accumulators: I will kill you later",
    "Decumulators: unwinding the unwindable",
    "Knock-out forwards: free leverage until it's not",
    "Range accruals: collecting pennies in a shrinking box",
    "Pivot TARFs: because regular TARFs weren't evil enough",

    # Autocallables & structured notes
    "Autocallables: early redemption for the house, bag holding for you",
    "Phoenix autocalls: rising from ashes, falling to losses",
    "Reverse convertibles: bond until it's stock, stock until it's worthless",
    "Principal protected notes: principal protected, returns aren't",

    # Digital/Binary options
    "Digital options: zero or hero, mostly zero",
    "One-touch digitals: touched once, regretted forever",
    "No-touch digitals: anxiety in option form",
    "Double no-touch: twice the anxiety",
    "Range digitals: stay in the box or lose everything",
    "Digital gamma: infinite in theory, painful in practice",

    # Exotic FX options
    "FX TARFs: sold to corporates, hedged by traders, understood by nobody",
    "Power reverse dual currency: words that mean nothing, losses that mean everything",
    "Quanto FX: because one currency wasn't enough risk",
    "Composite options: multiple underlyings, singular regret",
    "FX accumulators: accumulating losses since 2008",

    # Callable/Puttable structures
    "Bermudan options: American freedom with European restrictions",
    "Callable bonds: issuer's option, investor's problem",
    "Puttable swaps: optionality you'll never use",
    "Cancellable forwards: because commitment is hard",

    # Exotic vol products
    "Cliquet vol: ratcheting volatility, ratcheting pain",
    "Napoleon options: short guy, tall losses",
    "Timer options: vol budget that runs out too fast",
    "Realized variance options: path-dependent nightmares",

    # Structured product wisdom
    "Exotic options: where closed-form solutions go to die",
    "Structured products: complexity for fees, simplicity for losses",
    "Exotic pricing: Monte Carlo until it works",
    "Path dependency: history matters, models don't care",
    "Exotic hedging: theoretical in books, impossible in practice",
    "Structured notes: sold not bought",
    "Exotic risk: can't measure it, can't hedge it, can't explain it",
    "Payoff diagrams: beautiful in PowerPoint, ugly in P&L",
    "Exotic options desk: where quants become traders and traders become alcoholics",
    "Term sheet: 40 pages of ways to lose money",

    # Pricing exotics
    "Pricing exotics: garbage in, garbage out, fees in between",
    "Exotic model risk: the model is wrong, the price is worse",
    "Monte Carlo convergence: eventually wrong with confidence",
    "Finite difference methods: finite accuracy, infinite runtime",
    "Closed-form solution: exists in theory, useless in practice",
    "Numerical methods: when math gives up",
    "Calibration: fitting wrong models to bad data",

    # Hedging exotics
    "Delta hedging exotics: rearranging deck chairs",
    "Vega hedging path-dependent options: good luck",
    "Static replication: works in textbooks",
    "Dynamic hedging exotics: expensive and futile",
    "Barrier hedging: gamma spike at the worst time",
    "Exotic Greeks: calculated precisely, hedged poorly",

    # Exotic sales & structuring
    "Structured products: wrapping risk in complexity",
    "Exotic sales pitch: 'It's like a vanilla option, but...'",
    "Structuring desk: creating problems for traders to solve",
    "Tear sheet: making garbage look good since forever",
    "Payoff customization: client gets what they want, trader gets what they deserve",
    "Exotic bid-offer: wide enough to drive a truck through",

    # ========================================================================
    # VOL TRADING & VOL SURFACE
    # ========================================================================

    # Vol surface dynamics
    "Vol surface: flat in models, bumpy in reality",
    "Sticky strike vs sticky delta: wrong either way",
    "Vol smile: market's way of saying Black-Scholes is broken",
    "Skew dynamics: moves when you don't want it to",
    "Term structure: upward sloping until it inverts",
    "Vol surface arbitrage: free money that costs everything",
    "Local vol: smooth surface, rough P&L",
    "Stochastic vol: because constant vol was too optimistic",

    # Vol smile specifics
    "25-delta smile: where the real trading happens",
    "ATM vol: the only point that's liquid",
    "Wing vol: wide bid-offer, wider losses",
    "Smile interpolation: connecting dots, creating losses",
    "Smile extrapolation: guessing badly with confidence",
    "Flat smile: said no FX trader ever",
    "Smile arbitrage: exists in theory",

    # Vol models
    "SABR model: wrong but industry standard",
    "Heston model: stochastic vol, deterministic losses",
    "Local vol model: smooth in theory, jumpy in practice",
    "SVI parameterization: fitting smiles, creating frowns",
    "Dupire local vol: elegant math, ugly hedges",
    "Jump diffusion: because continuous paths were too simple",
    "Rough vol: fractional Brownian motion, integer losses",

    # Vol trading strategies
    "Vol carry: collecting premium until you don't",
    "Vol arbitrage: risk-free in theory, risky in practice",
    "Dispersion trading: long single names, short index, short patience",
    "Relative value vol: pairs trade that unpairs",
    "Vol momentum: chasing moves that reverse",
    "Vol mean reversion: works until it doesn't",
    "Calendar spread vol: theta positive, gamma negative, P&L uncertain",

    # Realized vs Implied
    "Realized vol: what actually happened",
    "Implied vol: what the market fears",
    "Vol risk premium: gap between fear and reality",
    "Realized-implied spread: the trade that never works",
    "Vol of vol: second-order fear",
    "Forward vol: implied vol's unreliable cousin",
    "Breakeven vol: the vol you'll never realize",

    # Vol regimes
    "Low vol regime: calm before the storm",
    "High vol regime: storm during the storm",
    "Vol clustering: bad news travels in packs",
    "Vol regime change: when your model breaks",
    "Persistent vol: high vol stays high until it doesn't",
    "Vol mean reversion: eventually, maybe, hopefully",

    # Vol surface construction
    "Vol surface calibration: fitting noise to noise",
    "Arbitrage-free surface: theoretically required, practically impossible",
    "Butterfly arbitrage: when your surface is broken",
    "Calendar arbitrage: when your term structure inverts",
    "No-arbitrage conditions: violated daily",
    "Surface smoothing: hiding problems, creating new ones",

    # Skew trading
    "Skew trade: right on direction, wrong on timing",
    "Risk reversal: the market's fear gauge",
    "Skew flattening: selling high, buying higher",
    "Skew steepening: when markets panic",
    "Skew carry: collecting pennies, risking dollars",
    "Put skew: always expensive, sometimes worth it",

    # Vol surface risk
    "Vega risk: first-order pain",
    "Volga risk: second-order suffering",
    "Vanna risk: cross-Greek catastrophe",
    "Smile risk: when the surface moves against you",
    "Skew risk: one-sided pain",
    "Term structure risk: when the curve inverts",

    # FX vol specifics
    "FX vol smile: symmetric in theory, skewed in practice",
    "Delta conventions: 25-delta means something different everywhere",
    "Premium-adjusted delta: because regular delta was too simple",
    "Spot delta vs forward delta: choose your poison",
    "Eskimos have 4 different ways of saying snow, FX has 4 different ways of saying ATM strike",
    "FX vol quotes: bid-offer wider than the smile",
    "ATMF vs ATMS: fighting over basis points",

    # Vol wisdom
    "Vol trading: buying fear, selling hope",
    "Implied vol: expensive insurance you hope to never use",
    "Vol surface: the map is not the territory",
    "Vol models: all wrong, some useful",
    "Vol hedging: expensive and imperfect",
    "Vol P&L: path-dependent and painful",
    "Long vol: right eventually, broke immediately",
    "Short vol: profitable until it's catastrophic",
    "Vol trading: where math meets market and loses",
    "The vol surface: 2D representation of 3D pain",
    "Gold gamma: shiny metal, sharp losses",
    "Equity vol surface: skewed, kinked, and expensive",
    "SPX gamma: what you're short at the worst time",
    "SPX options: where retail meets institutional and loses",
    "0DTE options: because weekly expiry wasn't degenerate enough",
    "SPX put skew: permanently expensive, occasionally worth it",
    "Swaptions: options on swaps, regrets on both",
    
    # Hedge Fund / Multistrat quotes
    "Multistrat: because losing money in multiple ways is more efficient",
    "Diversification: correlation goes to one when your AUM goes to zero",
    "Risk parity: equal risk of failure across all strategies",
    "Fundamental analysis: right direction, wrong decade",
    "Technical analysis: pretty charts, ugly P&L",
    "Discretionary trading: conviction until conviction is wrong",
    "Quantitative strategies: backtesting on training data, blowing up on real data",
    "Factor investing: yesterday's anomaly, today's crowded trade",
    "Stat arb: finding inefficiencies that don't exist",
    "Pairs trading: convergence eventually, just not before bankruptcy",
    "Mean reversion: works great until prices revert to zero",
    "Momentum: buying strength, selling weakness, wrong both ways",
    "Sector rotation: yesterday's winners, today's bag holders",
    "Merger arb: arbitraging away your existence",
    "Macro hedge fund: right thesis, wrong timing, right losses",
    "Long/short equity: long pain, short gains",
    "Hedge fund: taking 2 and 20 to underperform SPY",
    "Portfolio optimization: maximizing correlations, minimizing returns",
    "Rebalancing: selling winners, buying losers, systematically wrong",
    "Leverage: amplifying skill and stupidity in equal measure",
    "Drawdown: the only guaranteed return in investing",
    "Tail hedging: expensive insurance against the inevitable",
    "Crisis alpha: alpha that only works during crises",
    "Crowded trade: when everyone's right until everyone's wrong",
    "Redemption notice: the market's way of saying 'timing'",
    "Gamma is temporary, screenshots are forever",
    "Long gamma, short career expectancy",
    "Gamma doesn't care about your thesis",
    "The market giveth, gamma taketh away",
    "Gamma exposure: choose violence",
    "Gamma hedge completed, disaster postponed",
    "Every gamma trade starts as a good idea",
    "Gamma scalping: earning pennies, risking aneurysms",
    "Gamma is just leverage wearing glasses",
    "Short gamma, long explanations",
    "Vega always moves after you've hedged it",
    "Long vega, short confidence",
    "Vega P&L: now featuring random numbers",
    "Vol expansion: nature healing",
    "Vol compression: trader depression",
    "Vega doesn't hurt until it does",
    "Vol traders call it opportunity, accountants call it volatility",
    "Long vol: eventually correct, immediately unemployed",
    "Short vol: collecting premiums from future you",
    "Vega is just gamma with extra steps",
    "Theta: charging rent on borrowed hope",
    "Theta never misses payroll",
    "Theta harvest season",
    "Time decay: undefeated since forever",
    "Theta is the internship of P&L",
    "Weekend theta: thank you for your donation",
    "Theta positive, emotionally negative",
    "Theta: slow violence",
    "The clock is your biggest counterparty",
    "Every option expires worthless eventually",
    "Delta neutral, directionally confused",
    "Delta hedge first, ask questions later",
    "Your directional view is showing",
    "Delta: the gateway Greek",
    "Delta one, stress level one hundred",
    "Spot moved. There goes the hedge.",
    "Delta hedging: solving today's problem tomorrow",
    "Flat delta, not flat emotions",
    "The market chose a direction for me",
    "Delta is temporary, slippage is forever",
    "The smile is smiling at your losses",
    "Skew remembers every crisis",
    "Every surface is arbitrage-free until inspected",
    "The wings know things",
    "Skew is fear with decimal places",
    "Surface calibrated, reality uncooperative",
    "Smile fitting: curve fitting with consequences",
    "The surface moved because it felt like it",
    "Local vol, global pain",
    "Every skew trade becomes a timing trade",
    "Marked to market, judged by management",
    "The spreadsheet says yes",
    "The model says maybe",
    "Risk approved it. That's concerning.",
    "Nothing is more permanent than a temporary hedge",
    "The trade looked better yesterday",
    "Every position is a hedge against happiness",
    "I trust the model. I fear the market.",
    "The book is balanced, the trader isn't",
    "P&L explain pending divine intervention",
    "Assume normality, receive abnormal outcomes",
    "The error term has entered the chat",
    "Statistically significant, economically irrelevant",
    "The backtest was magnificent",
    "Out-of-sample is where dreams go to die",
    "Confidence interval: confidently wrong",
    "Regression found a relationship. Reality disagreed.",
    "Correlation: friendship until stress arrives",
    "The model converged. The trade didn't.",
    "Machine learning: fitting noise faster",
    "One more Greek should fix this",
    "There is always another Greek",
    "The Greeks send their regards",
    "Greek-neutral, problem-positive",
    "The hedge has hedges now",
    "Greeks explained everything except the losses",
    "Cross-greeks: collaborative suffering",
    "Higher-order Greeks, lower-order judgment",
    "The Greeks are strong with this loss",
    "Delta was never the problem",
    "Conviction peaks at the top",
    "The market heard your stop",
    "Every trader is a volatility seller eventually",
    "Patience is a position",
    "The trade worked until money was involved",
    "Your best trade was the one you didn't do",
    "FOMO is not a strategy",
    "Risk management ruins great stories",
    "Hope is not executable",
    "The market rewards humility eventually",
    "P&L is the final peer review",
    "Green days build confidence, red days build character",
    "Attribution complete, mystery remains",
    "Profit is temporary, screenshots are eternal",
    "Every drawdown starts small",
    "P&L: the universal language",
    "The market audited my assumptions",
    "Performance review by mark-to-market",
    "Today's alpha is tomorrow's beta",
    "The bonus is path dependent",
]


class QuoteGenerator:
    """
    Fully stateless random quote generator.
    No memory, no history, no bias.
    """

    def __init__(self, quotes: List[str]):
        self.quotes = quotes

    # ----------------------------
    # Core randomness
    # ----------------------------

    def get_random_quote(self, seed: Optional[int] = None) -> str:
        """Return a single fully random quote."""
        rng = random.Random(seed) if seed is not None else random
        return rng.choice(self.quotes)

    def get_random_quotes(self, n: int = 1, seed: Optional[int] = None) -> List[str]:
        """Return n random quotes (with replacement)."""
        rng = random.Random(seed) if seed is not None else random
        return [rng.choice(self.quotes) for _ in range(n)]

    def get_unique_random_quotes(self, n: int, seed: Optional[int] = None) -> List[str]:
        """Return n unique random quotes (without replacement)."""
        rng = random.Random(seed) if seed is not None else random
        n = min(n, len(self.quotes))
        return rng.sample(self.quotes, n)

    # ----------------------------
    # Filtered randomness (stateless)
    # ----------------------------

    def get_quote_by_keyword(self, keyword: str, seed: Optional[int] = None) -> str:
        """Return a random quote matching a keyword."""
        rng = random.Random(seed) if seed is not None else random

        matches = [q for q in self.quotes if keyword.lower() in q.lower()]

        if not matches:
            return rng.choice(self.quotes)

        return rng.choice(matches)

    def get_quotes_by_keywords(self, keywords: List[str], n: int = 1, seed: Optional[int] = None) -> List[str]:
        """Return random quotes matching any keyword."""
        rng = random.Random(seed) if seed is not None else random

        keywords = [k.lower() for k in keywords]

        matches = [
            q for q in self.quotes
            if any(k in q.lower() for k in keywords)
        ]

        if not matches:
            matches = self.quotes

        return [rng.choice(matches) for _ in range(n)]

    # ----------------------------
    # Category-based randomness
    # ----------------------------

    def get_category_quote(self, category: str, seed: Optional[int] = None) -> str:
        """Return a random quote from a category (stateless filter)."""

        rng = random.Random(seed) if seed is not None else random

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
        if not keywords:
            return rng.choice(self.quotes)

        matches = [
            q for q in self.quotes
            if any(k in q.lower() for k in keywords)
        ]

        return rng.choice(matches if matches else self.quotes)


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
