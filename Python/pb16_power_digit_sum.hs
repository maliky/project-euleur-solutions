digitSum :: Integer -> Int
digitSum num = sum $ map digitToInt (show num)

main :: IO ()
main = print $ digitSum (2^1000)

{-Ou en une ligne 
main = print . sum . map digitToInt . show $ 2^1000
-}


