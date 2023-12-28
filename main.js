
document.getElementById('addRowBtn').addEventListener('click', function() {
    const tableBody = document.querySelector('#couponTable tbody');
    const couponInput = document.getElementById('couponInput').value;
    const validityInput = document.getElementById('validityInput').value;
    
    if (couponInput && validityInput) {
      const newRow = document.createElement('tr');
      newRow.innerHTML = `
        <td>${couponInput}</td>
        <td>${validityInput}</td>
        <td><button onclick = "deleter(this)" class = "rowdel">Delete Row</button></td>
      `;
      tableBody.appendChild(newRow);
      //console.log(delcount);
      
      
      //code to send data to backend server 
      // format:-
      /*{
       "couponID": "ABC123",
       "validity": "2023-12-31"
    //}*/

      sendDataToBackend(couponInput, validityInput)
      
      // Clear input fields after adding row
      document.getElementById('couponInput').value = '';
      document.getElementById('validityInput').value = '';
    } else {
      alert('Please enter both Coupon ID and Validity');
    }
  });




function sendDataToBackend(couponID, validity) {
  // Replace 'your_backend_endpoint' with your actual backend API endpoint
  const endpoint = 'https://d72e-110-235-237-21.ngrok-free.app/create_coupon';

  fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      // Add any other headers if needed
    },
    body: JSON.stringify({ couponID, validity })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Handle success response from the backend
    console.log('Data sent successfully:', data);
  })
  .catch(error => {
    // Handle errors during fetch or from the backend
    console.error('Error sending data:', error);
  });
}


function getDatafromBackend(){
  const apiUrl = 'https://run.mocky.io/v3/01a8af6d-a0ad-4c4d-8147-e2bd61216c88';
  const api2Url = 'https://run.mocky.io/v3/fcff6d0d-e224-4c14-af25-7ee9f0e07f11';

  

  //.then(data => {
    // Access the parsed JSON data here
    //console.log(data)
    // const couponName = data.data[0].coupon_name;
    // const validityDate = data.data[0].validity;

    // console.log("Coupon Name:", couponName);
    // console.log("Validity Date:", validityDate);
  
  // .catch(error => {
  //   // Handle any errors that occurred during the fetch
  //   console.error('Fetch Error:', error);
  // });


  fetch(apiUrl)
  .then(response => {
    if(!response.ok){
      throw new Error ('Nahi mila mc');
    }
    return response.json();
  })
  .then(data => {
    console.log();
    const tableAPI = document.getElementById('couponTableBody');
    data.forEach((coupon, index) => {
    const couponID = coupon.couponID;
    const validityDate = coupon.validity;

    const newRow = document.createElement('tr');

    const idCell = document.createElement('td');
    idCell.textContent = couponID;

    const validityCell = document.createElement('td');
    validityCell.textContent = validityDate;

    const removecell = document.createElement('td');
    removecell.innerHTML = "<button onclick = deleter(this) class = rowdel>Delete Coupon</button>";


    newRow.appendChild(idCell);
    newRow.appendChild(validityCell);
    newRow.appendChild(removecell);

    tableAPI.appendChild(newRow);
  })

  })
  .catch(error => {
    console.error('Error:', error);
  });

}

document.getElementById("getData").addEventListener("click", function(){
  getDatafromBackend();
});

// function to delete the row
function deleter(btn){
  var row = btn.parentNode.parentNode;
  row.parentNode.removeChild(row);

  //delete the coupon from the db itself
  //do an delete an api call
  //to send:-
  //username ,coupon and validity
  //document.getElementById("couponTable").deleteRow(btn);
}




