document.addEventListener('DOMContentLoaded', function() {

    
    toggler = document.querySelector('#customSwitches')
    document.querySelector('#customSwitches').dataset.predict
    if(toggler.dataset.predict === "True"){
        toggler.checked = true
      } else {
          toggler.checked = false
      }
  // Use buttons to toggle between views
  //document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    toggler.addEventListener('change', () => toggle_prediction(toggler.dataset.post))
  
});



function toggle_prediction(model_id) {
    fetch(`/prediction_switch/${model_id}`)
    .then(response => console.log(response.json()))
          
}
  /*
function load_mailbox(mailbox) {

  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#display-view').style.display = 'none';
  
//  location.reload()
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

// get email specific to inbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
    console.log(emails);
    emails.forEach(element => {console.log(element)
    const el = document.createElement('div')
    
    array = [element.sender , element.subject, element.timestamp]

   el.innerHTML= `<strong>From</strong>: ${element.sender} <strong>Subject</strong>: ${element.subject} <strong>Timestamp</strong>: ${element.timestamp}`
    
    el.style.padding = "5px"


    el.style.border="groove"
    el.style.margin="10px"
    if(element.read === true){
      el.style.backgroundColor = "#E5E5E5"
    }
    else {
      el.style.backgroundColor = "white"
    }

    el.addEventListener('mouseover', function(){
      el.style.color="red"
    })
    el.addEventListener('mouseout', function(){
      el.style.color="rgb(0, 86, 110)"
    })

    el.addEventListener('click', function(){
      display_email(element.id, mailbox)
    });
    el.addEventListener('click', function(){
      fetch(`/emails/${element.id}` ,{
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
    })
    document.querySelector('#emails-view').append(el)
    
    });
      // ... do something else with emails ...
  }
  );
}

function display_email(email_id, mailbox){
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#display-view').style.display = 'block';
  content = document.querySelector('#display-view')
  content.innerHTML = ''
  
  btn = document.createElement("button")
 // btn.innerHTML = "my button"
  div = document.createElement("div")
  reply = document.createElement("button")
  reply.innerHTML="reply"
  
  div.setAttribute("id", "button-div");
    
    btn.className= "btn btn-sm btn-outline-primary";
    reply.className= "btn btn-sm btn-outline-primary";


    document.querySelector("#display-view").append(div)
    if(mailbox !=="sent"){
    document.querySelector("#button-div").append(btn)
    }
    document.querySelector("#button-div").append(reply)
    
  
  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      sender = document.createElement("h5")
      sender.innerHTML=`From: ${email.sender}`
      
      timestamp=document.createElement("h5")
      timestamp.innerHTML = `Timestamp: ${email.timestamp}`
     
      subject = document.createElement('h5')
      subject.innerHTML= `Subject: ${email.subject}`
      
      recipients = document.createElement("h5")
      recipients.innerHTML = `To: ${email.recipients}`
     
      
      document.querySelector('#display-view').append(sender)
      
      document.querySelector('#display-view').append(recipients)
     
      document.querySelector('#display-view').append(subject)   
     
      document.querySelector("#display-view").append(timestamp)

      // ... do something else with email ...

      body = document.createElement("p")
      body.innerHTML = email.body
      document.querySelector('#display-view').append(body)
            
      
      if(email.archived===false){
        btn.innerHTML="to achive"
        btn.addEventListener('click', function(){
          fetch(`/emails/${email.id}`, {
            method: 'PUT',
            body: JSON.stringify({
                archived: true
            })
          })
          load_mailbox('inbox');
          location.reload()
            
        })
      }else{
        btn.innerHTML="unarchive"
        btn.addEventListener('click', function(){
          fetch(`/emails/${email.id}`, {
            method: 'PUT',
            body: JSON.stringify({
                archived: false
            })
            
          })
          load_mailbox('inbox');
          location.reload()
        })

      }

      reply.addEventListener('click', function(){

        document.querySelector('#emails-view').style.display = 'none';
        document.querySelector('#compose-view').style.display = 'block';
        document.querySelector('#display-view').style.display = 'none';
      
        document.querySelector('#compose-recipients').value = email.sender;
        console.log(email.subject.substring(0,3)) 
        if(email.subject.substring(0,3)==="Re:"){
        document.querySelector('#compose-subject').value = email.subject
        } else{
          document.querySelector('#compose-subject').value =`Re: ${email.subject}`
        }
        document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote:
         ${email.body}`;
    
    
      })
   


  });

 
   
  

  }
 */