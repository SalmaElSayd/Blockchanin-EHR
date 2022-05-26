pragma solidity ^0.8.0;

contract VisitRecord{

   struct Visit{ 
      //    int256 patientId;
      //  int128 age;
      //  bytes32 weight;
      //  bytes32 height;
      //  string reason;
      //  string diagnosis;
      //  string referrals;
      //  string followUp;
      //  string labTests; //cbc, freet3
      // int128 initialBloodPressure;
      // int128 initialBloodGlucose;
      // int128 initialPulse;
      // int128 initialOxygenLevel;
      bytes visitData;
      string previousRecordHash;
   }

// constructor/function input
   // int256 _patientId,
   //  int128 _age,
   //  bytes32 _weight,
   //  bytes32 _height,
   //  string memory _reason,
   //  string memory _diagnosis,
   //  string memory _referrals,
   //  string memory _followUp,
   //  string memory _labTests,
   //  string memory _previousRecordHash,
   //  Measurements memory measurements

   Visit visit;
   function store(bytes memory _visitData, string memory _previousRecordHash) external{
   //  visit.patientId = _patientId;
   //  visit.age =     _age;
   //  visit.weight =     _weight;
   //  visit.height =     _height;
   //  visit.reason =     _reason;
   //  visit.diagnosis =     _diagnosis;
   //  visit.referrals =     _referrals;
   //  visit.followUp =     _followUp;
   //  visit.labTests =     _labTests; 
   //  visit.measurements.initialBloodPressure =     measurements.initialBloodPressure;
   //  visit.measurements.initialBloodGlucose =     measurements.initialBloodGlucose;
   //  visit.measurements.initialOxygenLevel =     measurements.initialOxygenLevel;
   //  visit.measurements.initialPulse =     measurements.initialPulse;
      visit.visitData = _visitData;
      visit.previousRecordHash = _previousRecordHash;
   }

   constructor(
    bytes memory _visitData,
    string memory _previousRecordHash
   ){
   //  visit.patientId = _patientId;
   //  visit.age =     _age;
   //  visit.weight =     _weight;
   //  visit.height =     _height;
   //  visit.reason =     _reason;
   //  visit.diagnosis =     _diagnosis;
   //  visit.referrals =     _referrals;
   //  visit.followUp =     _followUp;
   //  visit.labTests =     _labTests; 
   //  visit.measurements.initialBloodPressure =    _initialBloodPressure;
   //  visit.measurements.initialBloodGlucose =     _initialBloodGlucose;
   //  visit.measurements.initialPulse =     _initialPulse;
   //  visit.measurements.initialOxygenLevel =     _initialOxygenLevel;
    visit.previousRecordHash = _previousRecordHash;
    visit.visitData = _visitData;

   }


   function readRecord() public view returns(Visit memory){
      return visit;
   }
}