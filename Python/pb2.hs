-- sum of even valued terms in Fibonacci which do not exceed four million
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-2) + fib (n-1)

sumEvenFib :: Int -> Int
sumEvenFib 0 = 0
sumEvenFib 1 = 2
sumEvenFib 2 = 8
sumEvenFib n = 4 * sumEvenFib (n-1) + sumEvenFib (n-2)

-- Il faut trouver la position du term fibo qui n'excède pas 4 millions

