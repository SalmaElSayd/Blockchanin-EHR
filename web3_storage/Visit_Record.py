
class visit_record:
    def __init__(self, patientId, age, weight, height, reason, diagnosis, referrals, follow_up, lab_tests, blood_pressure, blood_glucose, pulse, oxygen_level):
        self.patientId = patientId
        self.age = age
        self.weight = weight
        self.height = height
        self.reason = reason
        self.diagnosis = diagnosis
        self.referrals = referrals
        self.follow_up = follow_up
        self.lab_tests = lab_tests
        self.blood_pressure = blood_pressure
        self.blood_glucose = blood_glucose
        self.pulse = pulse
        self.oxygen_level = oxygen_level

    def to_string(self):
        return (str(self.patientId)+"," +
                str(self.age)+"," +
                str(self.weight)+"," +
                str(self.height)+"," +
                str(self.reason)+"," +
                str(self.diagnosis)+"," +
                str(self.referrals)+"," +
                str(self.follow_up)+"," +
                str(self.lab_tests)+"," +
                str(self.blood_pressure)+"," +
                str(self.blood_glucose)+"," +
                str(self.pulse)+"," +
                str(self.oxygen_level))

    def to_byte(self):
        return bytes(self.to_string(), "UTF-8")

    def string2obj(self, data):
        patientId, age, weight, height, reason, diagnosis, referrals, follow_up, lab_tests, blood_pressure, blood_glucose, pulse, oxygen_level = data.split(
            ",")
        self.patientId = patientId
        self.age = age
        self.weight = weight
        self.height = height
        self.reason = reason
        self.diagnosis = diagnosis
        self.referrals = referrals
        self.follow_up = follow_up
        self.lab_tests = lab_tests
        self.blood_pressure = blood_pressure
        self.blood_glucose = blood_glucose
        self.pulse = pulse
        self.oxygen_level = oxygen_level
