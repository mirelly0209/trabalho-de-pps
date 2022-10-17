# trabalho-de-pps



<!DOCTYPE html>
<html>
<head>
  <title>My Page Title</title>
  <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
</head>
</html>




<!DOCTYPE hmtml>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE-edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Formulário | GN</title>
      <style>
          body{
              font-family: Arial, Helvetica, sans-serif;
              background-image: linear-gradient(to right, rgb(20, 147, 220), rgb(17, 54, 71));
          }
          .box{
              color: white;
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%,-50%);
              background-color: rgba(0, 0, 0, 0.6);
              padding: 15px;
              border-radius: 15px;
              width: 20%;
          }
          fieldset{
              border: 3px solid dodgerblue;
          }
          legend{
              border: 1px solid dodgerblue;
              padding: 10px;
              text-align: center;
              background-color: dodgerblue;
              border-radius: 8px;
          }
          .inputBox{
              position: relative;
          }
          .inputUser{
              background: none;
              border: none;
              border-bottom: 1px solid white;
              outline: none;
              color: white;
              font-size: 15px;
              width: 100%;
              letter-spacing: 2px;
            }
            .labelInput{
            position: absolute;
            top: 0;
            left: 10px;
            transition: .5s;
        }
        .inputUser:focus ~ .labelInput,
        .inputUser:valid ~ .labelInput{
            top: -15px;
            font-size: 12px;
            color: dodgerblue;
        }
        #data_nascimento{
            border: none;
            padding: 8px;
            border-radius: 10px;
            outline: none;
            font-size: 15px;
        }
        #submit{
            background-image: linear-gradient(to right, rgb(0, 92, 197), rgb(90, 20, 220));  
            width: 100px;
            border: none;
            padding: 15px;
            color: white;
            font-size: 15px;
            cursor: pointer;
            border-radius: 10px;
        }
      </style>
</head>
<body>
    <div class="box">
        <form action="">
            <fieldset>
                <legend><b>Formulário de funcionários</b></legend>    
                <br>
                <div class="inputBox">
                    <input type="text" name="nome" id="nome" class="inputUser" required>
                    <label for="nome" class="labelInput">Nome</label>
                </div>
                <br>
                <div class="inputBox">
                    <input type="text" name="email" id="email" class="inputUser" required>
                    <label for="email" class="labelInput">Email</label>
                </div>
                <br>
                <div class="inputBox">
                    <input type="tel" name="numero" id="numero" class="inputUser" required>
                    <label for="numero" class="labelInput">Número</label>
                </div>
                <br>
                <p>Sexo:</p>
                 <input type="radio" id="feminino" name="genero" value="feminino" required>
                 <label for="feminino">Feminino</label>
                 <br>
                 <input type="radio" id="masculino" name="genero" value="masculino" required>
                 <label for="masculino">Masculino</label>
                 <br><br>
                <label for="data_nascimento"><b>Data de nascimento:</b></label>
                <input type="date" name="data_nascimento" id="data_nascimento" required>
                <br>
                <div class="inputBox">
                    <input type="text" name="cidade" id="cidade" class="inputUser" required>
                    <label for="cidade" class="labelInput">Cidade</label>
                </div>
                <br><br>
                <input type="submit" name="submit" id="submit">

            </fieldset>  
        </form>
    </div>

</body>
</html>
