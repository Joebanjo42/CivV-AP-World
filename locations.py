from BaseClasses import Location


class CivVLocation(Location):
    game: str = "Civilization V"

# def get_location_id(key):
#     print(location_table_data[key])
                            #ID, Region
location_table_data = {
    "Pottery":              (1),
    "Animal Husbandry":     (2),
    "Archery":              (3),
    "Mining":               (4),
    "Sailing":              (5),
    "Calendar":             (6),
    "Writing":              (7),
    "Trapping":             (8),
    "The Wheel":            (9),
    "Masonry":              (10),
    "Bronze Working":       (11),
    "Optics":               (12),
    "Horseback Riding":     (13),
    "Mathematics":          (14),
    "Construction":         (15),
    "Philosophy":           (16),
    "Drama":                (17),
    "Currency":             (18),
    "Engineering":          (19),
    "Iron Working":         (20),
    "Theology":             (21),
    "Civil Service":        (22),
    "Guilds":               (23),
    "Metal Casting":        (24),
    "Compass":              (25),
    "Education":            (26),
    "Chivalry":             (27),
    "Machinery":            (28),
    "Physics":              (29),
    "Steel":                (30),
    "Astronomy":            (31),
    "Acoustics":            (32),
    "Banking":              (33),
    "Printing Press":       (34),
    "Gunpowder":            (35),
    "Navigation":           (36),
    "Architecture":         (37),
    "Economics":            (38),
    "Metallurgy":           (39),
    "Chemistry":            (40),
    "Archaeology":          (41),
    "Scientific Theory":    (42),
    "Industrialization":    (43),
    "Rifling":              (44),
    "Military Science":     (45),
    "Fertilizer":           (46),
    "Biology":              (47),
    "Electricity":          (48),
    "Steam Power":          (49),
    "Dynamite":             (50),
    "Refrigeration":        (51),
    "Radio":                (52),
    "Replaceable Parts":    (53),
    "Flight":               (54),
    "Railroad":             (55),
    "Plastics":             (56),
    "Electronics":          (57),
    "Ballistics":           (58),
    "Combustion":           (59),
    "Penicillin":           (60),
    "Atomic Theory":        (61),
    "Radar":                (62),
    "Combined Arms":        (63),
    "Ecology":              (64),
    "Nuclear Fission":      (65),
    "Rocketry":             (66),
    "Computers":            (67),
    "Telecommunications":   (68),
    "Mobile Tactics":       (69),
    "Advanced Ballistics":  (70),
    "Satellites":           (71),
    "Robotics":             (72),
    "Lasers":               (73),
    "The Internet":         (74),
    "Globalization":        (75),
    "Particle Physics":     (76),
    "Nuclear Fusion":      (77),
    "Nanotechnology":       (78),
    "Stealth":              (79)
}

# base_id = 0
# offset = 140319
# loc = {name : id for id, name in enumerate(location_table_data.values(), base_id + offset)}
# print(loc)



# location_table = {name:id for (name,id) in location_table_data.items()}
# newlocations = {name:id for (name,id) in enumerate(location_table_data.values(), base_id + offset)}
# print(newlocations[140319])