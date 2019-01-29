from main import run as getData
from function4 import func4

def main():
    # Get data dynamically based on the profiles listed from filepath
    sample_list = getData("./profiles/")
    print "For Michael:"
    print func4('Michael Jackso', sample_list) #first use case to test for wrong input
    print "\nFor Michael:"
    print func4('Michael Jackson', sample_list)
    print "\nFor Carol:"
    print func4('Carol', sample_list)
    print "\nFor Kevin:"
    print func4('Kevin', sample_list)
    print "\nFor Rose:"
    print func4('Rose', sample_list)
    print "\nFor Shelley:"
    print func4('Shelley', sample_list)
    print "\nFor Joel:"
    print func4('Joel Jackson', sample_list)
    print "\nFor Jenny:"
    print func4('Jenny Wang', sample_list)
    print "\nFor Angela:"
    print func4('Angela Little', sample_list)
    print "\nFor Lisa:"
    print func4('Lisa Marie', sample_list)
    print "\nFor Teresa:"
    print func4('Teresa', sample_list)


if __name__ == '__main__':
    main()
