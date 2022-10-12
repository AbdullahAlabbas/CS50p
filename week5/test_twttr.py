from twttr import shorten

def main():
    test_capital_cases()
    test_numbers()
    test_panctuation()

def test_capital_cases():
    
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItteR") == "TwttR"
    
def test_numbers():
    assert shorten("1234") =="1234"

def test_panctuation():
    assert shorten("!?.,") == "!?.,"
    
if __name__ == "__main__":
    main()