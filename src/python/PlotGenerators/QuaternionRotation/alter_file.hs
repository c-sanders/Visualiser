import System.Environment (getArgs)


main :: IO ()
main = do
    [inputFile, outputFile] <- getArgs

    contents <- readFile inputFile

    let newContents = unlines $
            map (\name -> "file '" ++ name ++ "'\n" ++ "duration 0.50") (lines contents)

    writeFile outputFile newContents