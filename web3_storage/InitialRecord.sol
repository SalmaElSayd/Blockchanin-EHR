pragma solidity ^0.8.0;

contract InitialRecord{

struct Data{
    //  int256 patientId;
    // string name;
    // int128 age;
    // int128 weight;
    // int128 height;
    // bool gender;
    // int128 initialBloodPressure;
    // int128 initialBloodGlucose;
    // int initialPulse;
    // int128 initialOxygenLevel;
    bytes patientData;
}

   Data patient;

// constructor/ method input
// int256 _patientId,
//     string memory _name,
//     int128 _age,
//     int128 _weight,
//     int128 _height,
//     bool _gender,
//     int128 _initialBloodPressure,
//     int128 _initialBloodGlucose,
//     int _initialPulse,
//     int128 _initialOxygenLevel

    constructor(bytes memory _patientData){

        // patient.patientId =_patientId ;
        // patient.name =_name ;
        // patient.age =_age ;
        // patient.weight =_weight ;
        // patient.height =_height ;
        // patient.gender =_gender ;
        // patient.initialBloodPressure =_initialBloodPressure ;
        // patient.initialBloodGlucose =_initialBloodGlucose ;
        // patient.initialPulse =_initialPulse ;
        // patient.initialOxygenLevel =_initialOxygenLevel ;
        patient.patientData = _patientData;

    } 

    function store(bytes memory _patientData) public {

        // patient.patientId =_patientId ;
        // patient.name =_name ;
        // patient.age =_age ;
        // patient.weight =_weight ;
        // patient.height =_height ;
        // patient.gender =_gender ;
        // patient.initialBloodPressure =_initialBloodPressure ;
        // patient.initialBloodGlucose =_initialBloodGlucose ;
        // patient.initialPulse =_initialPulse ;
        // patient.initialOxygenLevel =_initialOxygenLevel ;
        patient.patientData = _patientData;

    } 

    function readRecord() public view returns(Data memory){
        return patient;
    }


    function verifyTx() public view returns(bool r){

    }

}