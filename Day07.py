rankings = {
    "A": "m",
    "K": "l",
    "Q": "k",
    "J": "j",
    "T": "i",
    "9": "h",
    "8": "g",
    "7": "f",
    "6": "e",
    "5": "d",
    "4": "c",
    "3": "b",
    "2": "a"
}

joker_rankings = {
    "A": "m",
    "K": "l",
    "Q": "k",
    "T": "j",
    "9": "i",
    "8": "h",
    "7": "g",
    "6": "f",
    "5": "e",
    "4": "d",
    "3": "c",
    "2": "b",
    "J": "a"
}


def day07(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    hands = list()
    for line in lines:
        hand = Hand()
        parts = line.split(" ")
        hand.hand = parts[0]
        hand.bet = int(parts[1])
        hands.append(hand)

    if is_part_2:
        hands.sort(key=custom_compare_jokers)
    else:
        hands.sort(key=custom_compare)

    answer = 0
    for i in range(len(hands)):
        answer += (i + 1) * hands[i].bet

    return answer


def custom_compare(hand1):
    return hand1.rank(), hand1.strength()


def custom_compare_jokers(hand1):
    return hand1.part2_rank(), hand1.strengthWithJokers()


class Hand:
    def __int__(self):
        self.hand = ""
        self.bet = 0

    def rank(self):
        counts = dict()

        for letter in self.hand:
            if letter in counts:
                counts[letter] = counts[letter] + 1
            else:
                counts[letter] = 1

        if len(counts) == 1:
            return 7

        if len(counts) == 2:
            count_list = list()

            for key in counts:
                count_list.append(counts[key])

            if count_list[0] == 4 or count_list[1] == 4:
                return 6
            elif (count_list[0] == 3 and count_list[1] == 2) or (count_list[0] == 2 and count_list[1] == 3):
                return 5

        if len(counts) == 3:
            count_list = list()

            for key in counts:
                count_list.append(counts[key])

            if count_list[0] == 3 or count_list[1] == 3 or count_list[2] == 3:
                return 4

            return 3

        if len(counts) == 4:
            return 2

        return 1

    def part2_rank(self):
        calc_rank = self.rank()

        j_count = 0
        for letter in self.hand:
            if letter == "J":
                j_count = j_count + 1

        if j_count == 0:
            return calc_rank

        if calc_rank == 6:
            if j_count > 0:
                return 7
        elif calc_rank == 5:
            if j_count >= 2:
                return 7
        elif calc_rank == 4:
            if j_count == 3:
                return 6
            elif j_count == 1:
                return 6
        elif calc_rank == 3:
            if j_count == 2:
                return 6
            elif j_count == 1:
                return 5
        elif calc_rank == 2:
            if j_count == 2:
                return 4
            elif j_count == 1:
                return 4
        elif calc_rank == 1:
            if j_count > 0:
                return 2

        return calc_rank

    def rank_with_jokers(self):
        counts = dict()

        for letter in self.hand:
            if letter in counts:
                counts[letter] = counts[letter] + 1
            else:
                counts[letter] = 1

        if "J" in counts:
            best = 1
            for key in counts:
                if key != "J":
                    test_hand = Hand()
                    test_hand.hand = self.hand.replace("J", key)
                    result = test_hand.rank()
                    best = max(best, result)

            return best

        if len(counts) == 1:
            return 7

        if len(counts) == 2:
            count_list = list()

            for key in counts:
                count_list.append(counts[key])

            if count_list[0] == 4 or count_list[1] == 4:
                return 6
            elif (count_list[0] == 3 and count_list[1] == 2) or (count_list[0] == 2 and count_list[1] == 3):
                return 5

        if len(counts) == 3:
            count_list = list()

            for key in counts:
                count_list.append(counts[key])

            if count_list[0] == 3 or count_list[1] == 3 or count_list[2] == 3:
                return 4

            return 3

        if len(counts) == 4:
            return 2

        return 1

    def strength(self):
        answer = ""
        for letter in self.hand:
            answer += rankings[letter]

        return answer


    def strengthWithJokers(self):
        answer = ""
        for letter in self.hand:
            answer += joker_rankings[letter]

        return answer





