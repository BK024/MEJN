from collections import OrderedDict as OD
from Position import Position


class Board:
    play_position_od: OD
    finished_position_od: OD
    start_position_od: OD

    def __init__(self):
        self.play_position_od = None
        self.finished_position_od = None
        self.start_position_od = None

        # Fill the dicts
        self.make_position_dicts()

    def make_position_dicts(self):
        position_dict = OD()
        position_dict[1] = Position(1)
        position_dict[2] = Position(2)
        position_dict[3] = Position(3)
        position_dict[4] = Position(4)
        position_dict[5] = Position(5)
        position_dict[6] = Position(6)
        position_dict[7] = Position(7)
        position_dict[8] = Position(8)
        position_dict[9] = Position(9)
        position_dict[10] = Position(10)
        position_dict[11] = Position(11)
        position_dict[12] = Position(12)
        position_dict[13] = Position(13)
        position_dict[14] = Position(14)
        position_dict[15] = Position(15)
        position_dict[16] = Position(16)
        position_dict[17] = Position(17)
        position_dict[18] = Position(18)
        position_dict[19] = Position(19)
        position_dict[20] = Position(20)
        position_dict[21] = Position(21)
        position_dict[22] = Position(22)
        position_dict[23] = Position(23)
        position_dict[24] = Position(24)
        position_dict[25] = Position(25)
        position_dict[26] = Position(26)
        position_dict[27] = Position(27)
        position_dict[28] = Position(28)
        position_dict[29] = Position(29)
        position_dict[30] = Position(30)
        position_dict[31] = Position(31)
        position_dict[32] = Position(32)
        position_dict[33] = Position(33)
        position_dict[34] = Position(34)
        position_dict[35] = Position(35)
        position_dict[36] = Position(36)
        position_dict[37] = Position(37)
        position_dict[38] = Position(38)
        position_dict[39] = Position(39)
        position_dict[40] = Position(40)
        self.play_position_od = position_dict

        start_position_dict = OD()
        start_position_dict["green 1"] = Position(41)
        start_position_dict["green 2"] = Position(42)
        start_position_dict["green 3"] = Position(43)
        start_position_dict["green 4"] = Position(44)
        start_position_dict["red 1"] = Position(45)
        start_position_dict["red 2"] = Position(46)
        start_position_dict["red 3"] = Position(47)
        start_position_dict["red 4"] = Position(48)
        start_position_dict["yellow 1"] = Position(49)
        start_position_dict["yellow 2"] = Position(50)
        start_position_dict["yellow 3"] = Position(51)
        start_position_dict["yellow 4"] = Position(52)
        start_position_dict["blue 1"] = Position(53)
        start_position_dict["blue 2"] = Position(54)
        start_position_dict["blue 3"] = Position(55)
        start_position_dict["blue 4"] = Position(56)
        self.start_position_od = start_position_dict

        finished_position_dict = OD()
        finished_position_dict["green 1"] = Position(57)
        finished_position_dict["green 2"] = Position(58)
        finished_position_dict["green 3"] = Position(59)
        finished_position_dict["green 4"] = Position(60)
        finished_position_dict["red 1"] = Position(61)
        finished_position_dict["red 2"] = Position(62)
        finished_position_dict["red 3"] = Position(63)
        finished_position_dict["red 4"] = Position(64)
        finished_position_dict["yellow 1"] = Position(65)
        finished_position_dict["yellow 2"] = Position(66)
        finished_position_dict["yellow 3"] = Position(67)
        finished_position_dict["yellow 4"] = Position(68)
        finished_position_dict["blue 1"] = Position(69)
        finished_position_dict["blue 2"] = Position(70)
        finished_position_dict["blue 3"] = Position(71)
        finished_position_dict["blue 4"] = Position(72)
        self.finished_position_od = finished_position_dict