pragma solidity ^0.8.0;

contract VisitRecord{

   struct Visit{ 
      int256 patientId;
    int128 age;
    bytes32 weight;
    bytes32 height;
    string reason;
    string diagnosis;
    string referrals;
    string followUp;
    string labTests; //cbc, freet3
    string previousRecordHash;
    Measurements measurements;
   }

   struct Measurements {
      int128 initialBloodPressure;
      int128 initialBloodGlucose;
      int128 initialPulse;
      int128 initialOxygenLevel;
   }

   Visit visit;
   function store(
    int256 _patientId,
    int128 _age,
    bytes32 _weight,
    bytes32 _height,
    string memory _reason,
    string memory _diagnosis,
    string memory _referrals,
    string memory _followUp,
    string memory _labTests,
    string memory _previousRecordHash,
    Measurements memory measurements
   ) external{
    visit.patientId = _patientId;
    visit.age =     _age;
    visit.weight =     _weight;
    visit.height =     _height;
    visit.reason =     _reason;
    visit.diagnosis =     _diagnosis;
    visit.referrals =     _referrals;
    visit.followUp =     _followUp;
    visit.labTests =     _labTests; 
    visit.previousRecordHash = _previousRecordHash;
    visit.measurements.initialBloodPressure =     measurements.initialBloodPressure;
    visit.measurements.initialBloodGlucose =     measurements.initialBloodGlucose;
    visit.measurements.initialPulse =     measurements.initialPulse;
    visit.measurements.initialOxygenLevel =     measurements.initialOxygenLevel;

   }

   // constructor(
   //  int256 _patientId,
   //  int128 _age,
   //  bytes32 _weight,
   //  bytes32 _height,
   //  string memory _reason,
   //  string memory _diagnosis,
   //  string memory _referrals,
   //  string memory _followUp,
   //  string memory _labTests,
   //  string memory _previousRecordHash,
   //  int128 _initialBloodPressure,
   //    int128 _initialBloodGlucose,
   //    int128 _initialPulse,
   //    int128 _initialOxygenLevel
   // ){
   //  visit.patientId = _patientId;
   //  visit.age =     _age;
   //  visit.weight =     _weight;
   //  visit.height =     _height;
   //  visit.reason =     _reason;
   //  visit.diagnosis =     _diagnosis;
   //  visit.referrals =     _referrals;
   //  visit.followUp =     _followUp;
   //  visit.labTests =     _labTests; 
   //  visit.previousRecordHash = _previousRecordHash;
   //  visit.measurements.initialBloodPressure =    _initialBloodPressure;
   //  visit.measurements.initialBloodGlucose =     _initialBloodGlucose;
   //  visit.measurements.initialPulse =     _initialPulse;
   //  visit.measurements.initialOxygenLevel =     _initialOxygenLevel;

   // }


   function readRecord() public view returns(Visit memory){
      return visit;
   }
}