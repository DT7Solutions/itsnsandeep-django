
let contactform = document.querySelector('#contactForm');
let inputs = document.querySelectorAll('input')
let textariea = document.querySelector('textarea')
contactform.addEventListener('submit', function(event){
          event.preventDefault();
          $.ajax({
            type:'POST',
            url:'/',
            data:{
              name:$("#name").val(),
              email:$("#email").val(),
              message:$("#message").val(),
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
         
              swal("success", "Your Message was sending successfully ", "success");
            
            },
            error: function(xhr, status, error) {
              swal("error!", "Please Try Agian", "error");
            
            },
            dataType: 'text'
        })
        inputs.forEach(input => input.value = '');
        textariea.value =''


        Email.send({
          Host: "smtp.elasticemail.com",
          Username: "itsnsandeep123@gmail.com",
          Password: "4E28AA336E9DD7F0409536F7ED9D28631FEE",
          To: 'admin@itsnsandeep.com',
          From: "itsnsandeep123@gmail.com",
          Subject: subject,
          Body: "Name:" + fname + "<br/> For email:" + x + "<br/> Subject:" + subject + "<br/> Message:"
            + message
        }).then(
        alert("Sending email successfully....")
        );
      
      
});








