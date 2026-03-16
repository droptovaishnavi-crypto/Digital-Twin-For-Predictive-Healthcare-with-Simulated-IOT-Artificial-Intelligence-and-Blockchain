// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract HealthRecord {
    struct HeartData {
        uint256 heartRate;
        uint256 systolic;
        uint256 diastolic;
        uint256 temperature;
        uint256 respiratoryRate;
    }

    struct DiabetesData {
        uint256 pregnancies;
        uint256 glucose;
        uint256 bloodPressure;
        uint256 skinThickness;
        uint256 insulin;
        uint256 bmi;
        uint256 diabetesPedigreeFunction;
        uint256 age;
    }

    HeartData[] public heartRecords;
    DiabetesData[] public diabetesRecords;

    // ----------------- Heart -----------------
    function addHeartRecord(
        uint256 heartRate,
        uint256 systolic,
        uint256 diastolic,
        uint256 temperature,
        uint256 respiratoryRate
    ) public {
        heartRecords.push(
            HeartData(heartRate, systolic, diastolic, temperature, respiratoryRate)
        );
    }

    // ----------------- Diabetes -----------------
    function addDiabetesRecord(
        uint256 pregnancies,
        uint256 glucose,
        uint256 bloodPressure,
        uint256 skinThickness,
        uint256 insulin,
        uint256 bmi,
        uint256 diabetesPedigreeFunction,
        uint256 age
    ) public {
        diabetesRecords.push(
            DiabetesData(
                pregnancies,
                glucose,
                bloodPressure,
                skinThickness,
                insulin,
                bmi,
                diabetesPedigreeFunction,
                age
            )
        );
    }
}
