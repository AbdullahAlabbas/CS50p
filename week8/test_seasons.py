from seasons import check_birthday

def main():
    test_check_birthday()
    
    
def test_check_birthday():
    assert check_birthday("2003-08-29") == ("2003", "08", "29")
    assert check_birthday("2003-8-29") == None
    assert check_birthday("Aug 29, 2003") == None
    
    
if __name__ == "__main__":
    main()