
def day05(input_file, is_part_2):
    file = open(input_file, 'r')
    lines = file.readlines()

    seeds = list()
    seedToSoil = list()
    soilToFertilizer = list()
    fertilizerToWater = list()
    waterToLight = list()
    lightToTemperature = list()
    temperatureToHumidity = list()
    humidityToLocation = list()


    current_command = ""
    for line in lines:
        if line.startswith("seeds:"):
            numbers_text = line.replace("seeds: ", "")
            numbers_raw = numbers_text.split(" ")

            if is_part_2:
                i = 0
                while i < len(numbers_raw):
                    seed_range = Range()
                    seed_range.to_start = int(numbers_raw[i])
                    seed_range.count = int(numbers_raw[i + 1])
                    seeds.append(seed_range)
                    i = i + 2
            else:
                for number in numbers_raw:
                    seeds.append(int(number))

        elif line.startswith("seed-to-soil"):
            current_command = "seed-to-soil"
        elif line.startswith("soil-to-fertilizer"):
            current_command = "soil-to-fertilizer"
        elif line.startswith("fertilizer-to-water"):
            current_command = "fertilizer-to-water"
        elif line.startswith("water-to-light"):
            current_command = "water-to-light"
        elif line.startswith("light-to-temperature"):
            current_command = "light-to-temperature"
        elif line.startswith("temperature-to-humidity"):
            current_command = "temperature-to-humidity"
        elif line.startswith("humidity-to-location"):
            current_command = "humidity-to-location"
        elif len(line) < 2:
            continue #Blank Line
        else:
            parts = line.rstrip().split(" ")
            from_start = int(parts[1])
            to_start = int(parts[0])
            count = int(parts[2])

            target_list = list()

            if current_command == "seed-to-soil":
                target_list = seedToSoil
            elif current_command == "soil-to-fertilizer":
                target_list = soilToFertilizer
            elif current_command == "fertilizer-to-water":
                target_list = fertilizerToWater
            elif current_command == "water-to-light":
                target_list = waterToLight
            elif current_command == "light-to-temperature":
                target_list = lightToTemperature
            elif current_command == "temperature-to-humidity":
                target_list = temperatureToHumidity
            elif current_command == "humidity-to-location":
                target_list = humidityToLocation
            else:
                raise "Invalid command"

            item = Range()
            item.to_start = to_start
            item.from_start = from_start
            item.count = count

            target_list.append(item)

    min_location = 99999999999
    if is_part_2:
        i = 0
        while i < min_location:
            humidity = reverse_get(humidityToLocation, i)
            temperature = reverse_get(temperatureToHumidity, humidity)
            light = reverse_get(lightToTemperature, temperature)
            water = reverse_get(waterToLight, light)
            fertilizer = reverse_get(fertilizerToWater, water)
            soil = reverse_get(soilToFertilizer, fertilizer)
            seed = reverse_get(seedToSoil, soil)

            for some_range in seeds:
                min_value = some_range.to_start
                max_value = some_range.to_start + some_range.count - 1

                if seed >= min_value and seed <= max_value:
                    return i

            i += 1
    else:
        for seed in seeds:
            soil = get(seedToSoil, seed)
            fertilizer = get(soilToFertilizer, soil)
            water = get(fertilizerToWater, fertilizer)
            light = get(waterToLight, water)
            temperature = get(lightToTemperature, light)
            humidity = get(temperatureToHumidity, temperature)
            location = get(humidityToLocation, humidity)

            print(f"Location: {location}")
            min_location = min(location, min_location)

    return min_location



def get(range_list, key):
    for some_range in range_list:
        min_value = some_range.from_start
        max_value = some_range.count + some_range.from_start - 1

        if key >= min_value and key <= max_value:
            difference = key - min_value
            return some_range.to_start + difference

    return key

def reverse_get(range_list, key):
    for some_range in range_list:
        min_value = some_range.to_start
        max_value = some_range.to_start + some_range.count -1

        if key >= min_value and key <= max_value:
            difference = key - min_value
            return some_range.from_start + difference

    return key

class Range:
    def __init__(self):
        self.from_start = 0
        self.to_start = 0
        self.count = 0
