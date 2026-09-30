# 1:3.1 Precipitation

The daily precipitation generator is a Markov chain-skewed (Nicks, 1974) or Markov chain-exponential model (Williams, 1995). A first-order Markov chain is used to define the day as wet or dry. When a wet day is generated, a skewed distribution or exponential distribution is used to generate the precipitation amount. Table 1:3-1 lists SWAT+ input variables that are used in the precipitation generator.
