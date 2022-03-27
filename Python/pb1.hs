-- La somme des multiple de n inférieur à target
sumDivisibleBy :: Int -> Int -> Int
sumDivisibleBy target n = n * p * (p + 1) `div` 2
    where p = div target n

-- La somme des multiple de 3 et de 5 inférieur à 1000 peut s'écrire
-- t = 1000
-- sumDivisibleBy t 3 + sumDivisibleBy t 5 - sumDivisibleBy t 15
