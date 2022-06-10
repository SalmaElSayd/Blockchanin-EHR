# Blockchanin-EHR
The objective of the project is to create a blockchain application for Electronic Healthcare Records (EHR).
EHRs contain all information pertaining to a patient in the healthcare system. This includes general information about the patient (explained below)

For each patient, an initial transaction is to be added to a block in the blockchain that contains the general patient information. 
Then, for each visit a patient makes in the system, another transaction will be added to the most recent block with the information of that visit.
The transaction for each patient will be chained in a similar way to the transactions of a user on the Bitcoin blockchain. 
The following figure illustrates how the blockchain would look like after adding the EHR of one patient.

![Screenshot 2022-06-05 231705](https://user-images.githubusercontent.com/47950134/172070968-f5306204-084c-4309-9ff1-b65a4ab58c80.png)

## Basic Info contract
- name
- age
- weight
- height
- gender
- initial blood pressure
- inital blood glucose
- initial pulse
- initial oxygen level

## Visit contract
- any taken readings
- reason for the visit
- diagnosis
- perscription
- referrals
- follow-up
- appointments
- lab tests
- Additional Security Requirements

## Patient's data confidentiality:
- Only the patient's current doctor can access their records
- only Dr can write data
- Basic info can be written only once

## Programming language & Technologies:
- Python
- Ethereum
- Solidity
- Web3
- Flask

## UI templates
https://www.w3docs.com/learn-html/html-form-templates.html
https://alvarotrigo.com/blog/html-css-tabs/
