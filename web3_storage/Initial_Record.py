class initial_record:
    def __init__(self, patientId, name, age, weight, height, female, blood_pressure, blood_glucose, pulse, oxygen_level):
        self.patientId = patientId
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.female = female
        self.blood_pressure = blood_pressure
        self.blood_glucose = blood_glucose
        self.pulse = pulse
        self.oxygen_level = oxygen_level

    def to_string(self):
        return (str(self.patientId)+"," +
                self.name+"," +
                str(self.age)+"," +
                str(self.weight)+"," +
                str(self.height)+"," +
                str(self.female)+"," +
                str(self.blood_pressure)+"," +
                str(self.blood_glucose)+"," +
                str(self.pulse)+"," +
                str(self.oxygen_level))

    def to_byte(self):
        return bytes(self.to_string(), "UTF-8")

    def string2obj(self, data):
        patientId, name, age, weight, height, female, blood_pressure, blood_glucose, pulse, oxygen_level = data.split(
            ",")
        self.patientId = patientId
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.female = female
        self.blood_pressure = blood_pressure
        self.blood_glucose = blood_glucose
        self.pulse = pulse
        self.oxygen_level = oxygen_level