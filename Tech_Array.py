list_of_tech_keys = ["Pottery", "Animal Husbandry", "Archery", "Mining", "Sailing", "Calendar",
                      "Writing", "Trapping", "The Wheel", "Masonry", "Bronze Working",
                      "Optics", "Horseback Riding", "Mathematics", "Construction",
                      "Philosophy", "Drama", "Currency", "Engineering", "Iron Working",
                      "Theology", "Civil Service", "Guilds", "Metal Casting", "Compass",
                      "Education", "Chivalry", "Machinery", "Physics", "Steel", "Astronomy",
                      "Acoustics", "Banking", "Printing Press", "Gunpowder", "Navigation",
                      "Architecture", "Economics", "Metallurgy", "Chemistry", "Archaeology",
                      "Scientific Theory", "Industrialization", "Rifling", "Military Science", "Fertilizer",
                      "Biology", "Electricity", "Steam Power", "Dynamite", "Refrigeration", "Radio",
                      "Replaceable Parts", "Flight", "Railroad", "Plastic", "Electronics", "Ballistics", "Combustion",
                      "Penicilin", "Atomic Theory", "Radar", "Combined Arms", "Ecology", "Nuclear Fission", "Rocketry", "Computers",
                      "Telecommunications", "Mobile Tactics", "Advanced Ballistics", "Satellites", "Robotics", "Lasers",
                      "The Internet", "Globalization", "Particle Physics", "Nuclear Fusion", "Nanotechnology", "Stealth"]
tech_prereq_map_values = [[0], [0], [0], [0], [1], [1], [1], [2], [2, 3], [4], [4],
                         [5], [8, 9], [9], [9, 10], [6, 7] ,[7], [14], [14, 15], [11],
                         [16, 17], [13, 17, 18], [18], [19, 20], [12, 21], [21, 22], [22, 23], [23, 19], [24], [24],
                         [25, 26], [26], [26, 27], [27, 28, 29], [29, 30], [31], [32, 33], [33, 34], [34, 35], [35],
                         [36, 37], [37, 38], [38], [38, 39], [39, 40], [40], [41, 42], [42], [42, 43, 44], [45, 46],
                         [47, 48], [48], [48, 49], [49], [49, 50], [52, 53], [53, 54], [54, 55], [55],
                         [51, 56], [56, 57], [57, 58], [58, 59], [60, 61], [61, 62], [62], [62, 63],
                         [64], [64, 65], [65, 66], [66], [66, 67], [67], [68], [68], [68, 69, 70], [70, 71, 72], [72], [72, 73], [74, 75, 76, 77, 78, 79]]


list_of_items = {
    "Agriculture" : {
        "Type" : "TECH_AGRICULTURE",
        "Era" : "ERA_ANCIENT",
        "GridX" : "0",
        "GridY" : "5",
        "Cost" : "20",
        "Id" : "0"
    },
    "Pottery" :{
        "Type" : "TECH_POTTERY",
        "Era" : "ERA_ANCIENT",
        "GridX" : "1",
        "GridY" : "1",
        "Cost" : "35",
        "Id" : "1"
    },
    "Animal Husbandry" : {
        "Type" : "TECH_ANIMAL_HUSBANDRY",
        "Era" : "ERA_ANCIENT",
        "GridX" : "1",
        "GridY" : "4",
        "Cost" : "35",
        "Id" : "2"
    },
    "Archery" : {
        "Type" : "TECH_ARCHERY",
        "Era" : "ERA_ANCIENT",
        "GridX" : "1",
        "GridY" : "6",
        "Cost" : "35",
        "Id" : "3"      
    },
    "Mining" : {
        "Type" : "TECH_MINING",
        "Era" : "ERA_ANCIENT",
        "GridX" : "1",
        "GridY" : "8",
        "Cost" : "35",
        "Id" : "4"
    },
    "Sailing" : {
        "Type" : "TECH_SAILING",
        "Era" : "ERA_ANCIENT",
        "GridX" : "2",
        "GridY" : "0",
        "Cost" : "55",
        "Id" : "5"
    },
    "Calendar" : {
        "Type" : "TECH_CALENDAR",
        "Era" : "ERA_ANCIENT",
        "GridX" : "2",
        "GridY" : "1",
        "Cost" : "55",
        "Id" : "6"
    },
    "Writing" : {
        "Type" : "TECH_WRITING",
        "Era" : "ERA_ANCIENT",
        "GridX" : "2",
        "GridY" : "2",
        "Cost" : "55",
        "Id" : "7"
    },
    "Trapping" : {
        "Type" : "TECH_TRAPPING",
        "Era" : "ERA_ANCIENT",
        "GridX" : "2",
        "GridY" : "4",
        "Cost" : "55",
        "Id" : "8"
    },
    "The Wheel" : {
        "Type" : "TECH_THE_WHEEL",
        "Era" : "ERA_ANCIENT",
        "GridX" : "2",
        "GridY" : "6",
        "Cost" : "55",
        "Id" : "9"
    },
    "Masonry" : {
        "Type" : "TECH_MASONRY",
        "Era" : "ERA_ANCIENT",
        "GridX" : "2",
        "GridY" : "8",
        "Cost" : "55",
        "Id" : "10"
    },
    "Bronze Working" : {
        "Type" : "TECH_BRONZE_WORKING",
        "Era" : "ERA_ANCIENT",
        "GridX" : "2",
        "GridY" : "9",
        "Cost" : "55",
        "Id" : "11"
    },
    "Optics" : {
        "Type" : "TECH_OPTICS",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "3",
        "GridY" : "0",
        "Cost" : "85",
        "Id" : "12"
    },
    "Horseback Riding" : {
        "Type" : "TECH_HORSEBACK_RIDING",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "3",
        "GridY" : "4",
        "Cost" : "105",
        "Id" : "13"
    },
    "Mathematics" : {
        "Type" : "TECH_MATHEMATICS",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "3",
        "GridY" : "6",
        "Cost" : "105",
        "Id" : "14"
    },
    "Construction" : {
        "Type" : "TECH_CONSTRUCTION",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "3",
        "GridY" : "8",
        "Cost" : "105",
        "Id" : "15"
    },
    "Philosophy" : {
        "Type" : "TECH_PHILOSOPHY",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "4",
        "GridY" : "1",
        "Cost" : "175",
        "Id" : "16"
    },
    "Drama" : {
        "Type" : "TECH_DRAMA",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "4",
        "GridY" : "2",
        "Cost" : "175",
        "Id" : "17"
    },
    "Currency" : {
        "Type" : "TECH_CURRENCY",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "4",
        "GridY" : "6",
        "Cost" : "175",
        "Id" : "18"
    },
    "Engineering" : {
        "Type" : "TECH_ENGINEERING",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "4",
        "GridY" : "7",
        "Cost" : "175",
        "Id" : "19"
    },
    "Iron Working" : {
        "Type" : "TECH_IRON_WORKING",
        "Era" : "ERA_CLASSICAL",
        "GridX" : "4",
        "GridY" : "9",
        "Cost" : "175",
        "Id" : "20"
    },
    "Theology" : {
        "Type" : "TECH_THEOLOGY",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "5",
        "GridY" : "1",
        "Cost" : "275",
        "Id" : "21"
    },
    "Civil Service" : {
        "Type" : "TECH_CIVIL_SERVICE",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "5",
        "GridY" : "4",
        "Cost" : "275",
        "Id" : "22"
    },
    "Guilds" : {
        "Type" : "TECH_GUILDS",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "5",
        "GridY" : "6",
        "Cost" : "275",
        "Id" : "23"
    },
    "Metal Casting" : {
        "Type" : "TECH_METAL_CASTING",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "5",
        "GridY" : "8",
        "Cost" : "275",
        "Id" : "24"
    },
    "Compass" : {
        "Type" : "TECH_COMPASS",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "6",
        "GridY" : "0",
        "Cost" : "375",
        "Id" : "25"
    },
    "Education" : {
        "Type" : "TECH_EDUCATION",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "6",
        "GridY" : "2",
        "Cost" : "485",
        "Id" : "26"
    },
    "Chivalry" : {
        "Type" : "TECH_CHIVALRY",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "6",
        "GridY" : "5",
        "Cost" : "485",
        "Id" : "27"
    },
    "Machinery" : {
        "Type" : "TECH_MACHINERY",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "6",
        "GridY" : "7",
        "Cost" : "485",
        "Id" : "28"
    },
    "Physics" : {
        "Type" : "TECH_PHYSICS",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "6",
        "GridY" : "8",
        "Cost" : "485",
        "Id" : "29"
    },
    "Steel" : {
        "Type" : "TECH_STEEL",
        "Era" : "ERA_MEDIEVAL",
        "GridX" : "6",
        "GridY" : "9",
        "Cost" : "485",
        "Id" : "30"
    },
    "Astronomy" : {
        "Type" : "TECH_ASTRONOMY",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "7",
        "GridY" : "1",
        "Cost" : "780",
        "Id" : "31"
    },
    "Acoustics" : {
        "Type" : "TECH_ACOUSTICS",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "7",
        "GridY" : "3",
        "Cost" : "780",
        "Id" : "32"
    },
    "Banking" : {
        "Type" : "TECH_BANKING",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "7",
        "GridY" : "5",
        "Cost" : "780",
        "Id" : "33"
    },
    "Printing Press" : {
        "Type" : "TECH_PRINTING_PRESS",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "7",
        "GridY" : "7",
        "Cost" : "780",
        "Id" : "34"
    },
    "Gunpowder" : {
        "Type" : "TECH_GUNPOWDER",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "7",
        "GridY" : "9",
        "Cost" : "780",
        "Id" : "35",
    },
    "Navigation" : {
        "Type" : "TECH_NAVIGATION",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "8",
        "GridY" : "1",
        "Cost" : "1150",
        "Id" : "36"
    },
    "Architecture" : {
        "Type" : "TECH_ARCHITECTURE",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "8",
        "GridY" : "3",
        "Cost" : "1150",
        "Id" : "37"
    },
    "Economics" : {
        "Type" : "TECH_ECONOMICS",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "8",
        "GridY" : "5",
        "Cost" : "1150",
        "Id" : "38"
    },
    "Metallurgy" : {
        "Type" : "TECH_METALLURGY",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "8",
        "GridY" : "8",
        "Cost" : "1150",
        "Id" : "39"
    },
    "Chemistry" : {
        "Type" : "TECH_CHEMISTRY",
        "Era" : "ERA_RENAISSANCE",
        "GridX" : "8",
        "GridY" : "9",
        "Cost" : "1150",
        "Id" : "40"
    },
    "Archaeology" : {
        "Type" : "TECH_ARCHAEOLOGY",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "9",
        "GridY" : "1",
        "Cost" : "1600",
        "Id" : "41"
    },
    "Scientific Theory" : {
        "Type" : "TECH_SCIENTIFIC_THEORY",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "9",
        "GridY" : "3",
        "Cost" : "1600",
        "Id" : "42"
    },
    "Industrialization" : {
        "Type" : "TECH_INDUSTRIALIZATION",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "9",
        "GridY" : "5",
        "Cost" : "1600",
        "Id" : "430"
    },
    "Rifling" : {
        "Type" : "TECH_RIFLING",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "9",
        "GridY" : "6",
        "Cost" : "1600",
        "Id" : "44"
    },
    "Military Science" : {
        "Type" : "TECH_MILITARY_SCIENCE",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "9",
        "GridY" : "8",
        "Cost" : "1600",
        "Id" : "45"
    },
    "Fertilizer" : {
        "Type" : "TECH_FERTILIZER",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "9",
        "GridY" : "9",
        "Cost" : "1600",
        "Id" : "46"
    },
    "Biology" : {
        "Type" : "TECH_BIOLOGY",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "10",
        "GridY" : "1",
        "Cost" : "2350",
        "Id" : "47"
    },
    "Electricity" : {
        "Type" : "TECH_ELECTRICITY",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "10",
        "GridY" : "2",
        "Cost" : "2350",
        "Id" : "48"
    },
    "Steam Power" : {
        "Type" : "TECH_STEAM_POWER",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "10",
        "GridY" : "5",
        "Cost" : "2350",
        "Id" : "49"
    },
    "Dynamite" : {
        "Type" : "TECH_DYNAMITE",
        "Era" : "ERA_INDUSTRIAL",
        "GridX" : "10",
        "GridY" : "8",
        "Cost" : "2350",
        "Id" : "50"
    },
    "Refrigeration" : {
        "Type" : "TECH_REFRIGERATION",
        "Era" : "ERA_MODERN",
        "GridX" : "11",
        "GridY" : "1",
        "Cost" : "3100",
        "Id" : "51"
    },
    "Radio" : {
        "Type" : "TECH_RADIO",
        "Era" : "ERA_MODERN",
        "GridX" : "11",
        "GridY" : "2",
        "Cost" : "3100",
        "Id" : "52"
    },
    "Replaceable Parts" : {
        "Type" : "TECH_REPLACEABLE_PARTS",
        "Era" : "ERA_MODERN",
        "GridX" : "11",
        "GridY" : "3",
        "Cost" : "3100",
        "Id" : "53"
    },
    "Flight" : {
        "Type" : "TECH_FLIGHT",
        "Era" : "ERA_MODERN",
        "GridX" : "11",
        "GridY" : "5",
        "Cost" : "3100",
        "Id" : "54"
    },
    "Railroad" : {
        "Type" : "TECH_RAILROAD",
        "Era" : "ERA_MODERN",
        "GridX" : "11",
        "GridY" : "7",
        "Cost" : "3100",
        "Id" : "55"
    },
    "Plastic" : {
        "Type" : "TECH_PLASTIC",
        "Era" : "ERA_MODERN",
        "GridX" : "12",
        "GridY" : "2",
        "Cost" : "4100",
        "Id" : "56"
    },
    "Electronics" : {
        "Type" : "TECH_ELECTRONICS",
        "Era" : "ERA_MODERN",
        "GridX" : "12",
        "GridY" : "4",
        "Cost" : "4100",
        "Id" : "57"
    },
    "Ballistics" : {
        "Type" : "TECH_BALLISTICS",
        "Era" : "ERA_MODERN",
        "GridX" : "12",
        "GridY" : "5",
        "Cost" : "4100",
        "Id" : "58"
    },
    "Combustion" : {
        "Type" : "TECH_COMBUSTION",
        "Era" : "ERA_MODERN",
        "GridX" : "12",
        "GridY" : "7",
        "Cost" : "4100",
        "Id" : "59"
    },
    "Penicilin" : {
        "Type" : "TECH_PENICILIN",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "13",
        "GridY" : "1",
        "Cost" : "5100",
        "Id" : "60"
    },
    "Atomic Theory" : {
        "Type" : "TECH_ATOMIC_THEORY",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "13",
        "GridY" : "3",
        "Cost" : "5100",
        "Id" : "61"
    },
    "Radar" : {
        "Type" : "TECH_RADAR",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "13",
        "GridY" : "5",
        "Cost" : "5100",
        "Id" : "62"
    },
    "Combined Arms" : {
        "Type" : "TECH_COMBINED_ARMS",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "13",
        "GridY" : "7",
        "Cost" : "5100",
        "Id" : "63"
    },
    "Ecology" : {
        "Type" : "TECH_ECOLOGY",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "14",
        "GridY" : "1",
        "Cost" : "6400",
        "Id" : "64"
    },
    "Nuclear Fission" : {
        "Type" : "TECH_NUCLEAR_FISSION",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "14",
        "GridY" : "3",
        "Cost" : "6400",
        "Id" : "65"
    },
    "Rocketry" : {
        "Type" : "TECH_ROCKETRY",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "14",
        "GridY" : "5",
        "Cost" : "6400",
        "Id" : "66"
    },
    "Computers" : {
        "Type" : "TECH_COMPUTERS",
        "Era" : "ERA_POSTMODERN",
        "GridX" : "14",
        "GridY" : "7",
        "Cost" : "6400",
        "Id" : "67"
    },
    "Telecommunications" : {
        "Type" : "TECH_TELECOM",
        "Era" : "ERA_FUTURE",
        "GridX" : "15",
        "GridY" : "1",
        "Cost" : "7700",
        "Id" : "68"
    },
    "Mobile Tactics" : {
        "Type" : "TECH_MOBILE_TACTICS",
        "Era" : "ERA_FUTURE",
        "GridX" : "15",
        "GridY" : "2",
        "Cost" : "7700",
        "Id" : "68"
    },
    "Advanced Ballistics" : {
        "Type" : "TECH_ADVANCED_BALLISTICS",
        "Era" : "ERA_FUTURE",
        "GridX" : "15",
        "GridY" : "4",
        "Cost" : "7700",
        "Id" : "70"
    },
    "Satellites" : {
        "Type" : "TECH_SATELLITES",
        "Era" : "ERA_FUTURE",
        "GridX" : "15",
        "GridY" : "5",
        "Cost" : "7700",
        "Id" : "71"
    },
    "Robotics" : {
        "Type" : "TECH_ROBOTICS",
        "Era" : "ERA_FUTURE",
        "GridX" : "15",
        "GridY" : "6",
        "Cost" : "7700",
        "Id" : "72"
    },
    "Lasers" : {
        "Type" : "TECH_LASERS",
        "Era" : "ERA_FUTURE",
        "GridX" : "15",
        "GridY" : "7",
        "Cost" : "7700",
        "Id" : "73"
    },
    "The Internet" : {
        "Type" : "TECH_INTERNET",
        "Era" : "ERA_FUTURE",
        "GridX" : "16",
        "GridY" : "0",
        "Cost" : "8800",
        "Id" : "74"
    },
    "Globalization" : {
        "Type" : "TECH_GLOBALIZATION",
        "Era" : "ERA_FUTURE",
        "GridX" : "16",
        "GridY" : "1",
        "Cost" : "8800",
        "Id" : "75"
    },
    "Particle Physics" : {
        "Type" : "TECH_PARTICLE_PHYSICS",
        "Era" : "ERA_FUTURE",
        "GridX" : "16",
        "GridY" : "2",
        "Cost" : "8800",
        "Id" : "76"
    },
    "Nuclear Fusion" : {
        "Type" : "TECH_NUCLEAR_FUSION",
        "Era" : "ERA_FUTURE",
        "GridX" : "16",
        "GridY" : "5",
        "Cost" : "8800",
        "Id" : "77"
    },
    "Nanotechnology" : {
        "Type" : "TECH_NANOTECHNOLOGY",
        "Era" : "ERA_FUTURE",
        "GridX" : "16",
        "GridY" : "6",
        "Cost" : "8800",
        "Id" : "78"
    },
    "Stealth" : {
        "Type" : "TECH_STEALTH",
        "Era" : "ERA_FUTURE",
        "GridX" : "16",
        "GridY" : "7",
        "Cost" : "8800",
        "Id" : "79"
    },
    "Future Tech" : {
        "Type" : "TECH_FUTURE_TECH",
        "Era" : "ERA_FUTURE",
        "GridX" : "17",
        "GridY" : "4",
        "Cost" : "9500",
        "Id" : "80"
    },
}



# base_id = 140319  # Starting ID
# mygame_items = ["sword", "shield", "potion", "armor"]

# # Create the dictionary
# item_name_to_id = {name: id for id, name in enumerate(list_of_tech_keys, base_id)}

# print(item_name_to_id)