import re


def day15(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    data = lines[0]
    parts = data.split(",")
    answer = 0
    if is_part_2:
        boxes = list()
        lens_list = list()

        for i in range(256):
            box = Box()
            box.box_num = i
            boxes.append(box)

        for part in parts:
            lens_list.append(Lens(part))

        for lens in lens_list:
            box = boxes[lens.hash]

            if lens.operation == "=":
                found = False
                for i in range(len(box.lens)):
                    box_lens = box.lens[i]
                    if box_lens.label == lens.label:
                        box.lens[i] = lens
                        found = True

                if not found:
                    box.lens.append(lens)
            elif lens.operation == "-":
                new_lens = list()
                box = boxes[lens.hash]

                match = False
                for current_lens in box.lens:
                    if not match and current_lens.label == lens.label:
                        match = True
                        continue

                    new_lens.append(current_lens)

                box.lens = new_lens
            else:
                raise "Invalid operation"

        for box in boxes:
            lens_num = 1
            for current_lens in box.lens:
                answer += (box.box_num + 1) * lens_num * current_lens.focal_length
                lens_num += 1

    else:
        for part in parts:
            answer += make_hash(part)

    return answer


def make_hash(input):
    current = 0
    for char in input:
        ascii_code = ord(char)
        current += ascii_code
        current = current * 17
        current = current % 256

    return current


class Box:
    def __init__(self):
        self.box_num = 0
        self.lens = list()


class Lens:
    def __init__(self, data):
        self.label = ""
        self.hash = 0
        self.operation = ""
        self.focal_length = 0

        match = re.search(r"([a-z]+)=(\d+)", data)
        if match:
            self.label = match.group(1)
            self.focal_length = int(match.group(2))
            self.operation = "="

            self.hash = make_hash(self.label)
        else:
            match = re.search(r"([a-z]+)-", data)
            if match:
                self.label = match.group(1)
                self.hash = make_hash(self.label)
                self.operation = "-"
            else:
                raise "Invalid data"

