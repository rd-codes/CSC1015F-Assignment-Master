# A program to count the number of votes for each political party in an election
# 24 May 2021

# Return votes in alphabetical order
def sort():
    votes = []
    while "DONE" not in votes:
        party = input()
        votes.append(party)
    votes.remove("DONE")  # Remove DONE since it shouldn't be part of the list of votes
    return sorted(votes)


# Count the votes
def count():
    sorted_votes = sort()
    print()
    print("Vote counts:")

    # Ensure that votes that are counted are all removed from the vote list
    for party in sorted_votes[:]:
        num_votes = sorted_votes.count(party)
        while party in sorted_votes[:]:
            sorted_votes.remove(party)
        if num_votes != 0:
            print("{:<10}".format(party), " - ", num_votes, sep="")


def main():
    title = "Independent Electoral Commission"
    print(title, "-" * len(title), sep="\n")
    print("Enter the names of parties (terminated by DONE):")
    count()


if __name__ == "__main__":
    main()

