pragma solidity ^0.8.0;

contract InitialRecord{

struct Data{
     int256 patientId;
    string name;
    int128 age;
    bytes32 weight;
    bytes32 height;
    bool gender;
    bytes32 initialBloodPressure;
    bytes32 initialBloodGlucose;
    int initialPulse;
    bytes32 initialOxygenLevel;
}

   Data patient;



    function store(int256 _patientId,  
    string memory _name,
    int128 _age,
    bytes32 _weight,
    bytes32 _height,
    bool _gender,
    bytes32 _initialBloodPressure,
    bytes32 _initialBloodGlucose,
    int _initialPulse,
    bytes32 _initialOxygenLevel) external {

        patient.patientId =_patientId ;
        patient.name =_name ;
        patient.age =_age ;
        patient.weight =_weight ;
        patient.height =_height ;
        patient.gender =_gender ;
        patient.initialBloodPressure =_initialBloodPressure ;
        patient.initialBloodGlucose =_initialBloodGlucose ;
        patient.initialPulse =_initialPulse ;
        patient.initialOxygenLevel =_initialOxygenLevel ;

    } 

    function readRecord() public view returns(Data memory){
        return patient;
    }

}