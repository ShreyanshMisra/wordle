# Analyzing Wordle

An exploratory analysis of wordle that focuses on finding the best starter word in the game. It led to the development of an algorithm that can solve wordle using logic rules.
## Introduction
This investigation involved graphing a variety of strategies (vowel frequency, letter frequency, brute-force) on a dataset of 13,000+ words to find wordle's best starter word. 

An optimal starter eliminates the maximum number of words from the dataset, narrowing down the list of possible answers. I created a backtesting function that returns the percentage of of words that a starter eliminates from the dataset.

```python
def backtest(starter, dataset):
    total = len(dataset)
    eliminated = 0
    
    for word in dataset:
        for i in range(5):
            if starter[i] in word:
                eliminated += 1
                break
    pct = round(100 - ((total - eliminated)/total*100), 2)
    return starter, ("{}%".format(pct))
```
## Results
While the most optimal words from the vowel frequency and letter frequency strategy eliminated 93.35% and 95.55% words from the dataset respectively, the optimal word according to the brute force strategy, `toeas`, eliminated 95.72% words from the dataset.

Despite being the most optimal starter, `toeas` only appears in the `accepted` dataset and does not appear in the `answers` dataset. This is because while `toeas` is accepted as a guess, it will never be the actual solution to a wordle and using it as a starter word prevents you from ever guessing the wordle in one attempt.

When we use the brute force strategy on the `answers` dataset, we find that the most optimal word is `arise` which eliminates 92.74% of words in the dataset. While `arise` has a lower percentage of words eliminated when compared to `toeas`, it is present in the `answers` dataset and is in rotation to be the solution to a wordle sometime in the future.
## Files
- `datasets/`
- `analysis.ipynb` 
- `solver.py`
