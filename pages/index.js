import { Box, Button, Text, TextField, Image } from '@skynexui/components'; //é possível trazer ele todo mas não é necessário
import appConfig from "../config.json"
import { useRouter } from 'next/router';      //Sistema de roteamento do Next
import React from 'react';

/* 
# CSS in JS
## Prós
- O próprio JS sinaliza erros de coisa de "tema" da sua aplicação e mudanças gerais
## Contras
- É mais um JavaScript rodando no navegador processando coisas concorrendo com tudo
- Se o time (empresa) manja "menos" de CSS tem menos bugs

*/


function Title(props) {
  const Tag = props.tag || 'h1';
  return (
    <>
      <Tag>{props.children}</Tag>
      <style jsx>{`
            ${Tag} {
                color: ${appConfig.theme.colors.neutrals['000']};
                font-size: 24px;
                font-weight: 600;
            }
            `}</style>
    </>
  );
}

export default function PaginaInicial() {
  const roteamento = useRouter();           //Userouter() é um hook para fazer algo, no caso mudança de página

  const [username, setUserName] = React.useState('RafaelAndradeDev');
  const [location, setLocation] = React.useState('Ceará - Brazil');
  const [followers, setFollowers] = React.useState('0');

  function handleChangeUsername(event) {
    setUserName(event.target.value);

    if (event.target.value.length >= 3) {
      fetch(`https://api.github.com/users/${event.target.value}`)
        .then(response => response.json())
        .then(data => {
          // console.log('retorno fetch usuário: ', data);
          setLocation(data.location || '');
          setFollowers(data.followers || '');

        });
    }
  }



  return (
    <>
      <Box
        styleSheet={{
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          backgroundColor: appConfig.theme.colors.primary['000'],
          backgroundImage: 'url(https://virtualbackgrounds.site/wp-content/uploads/2020/08/the-matrix-digital-rain.jpg)',
          backgroundRepeat: 'no-repeat', backgroundSize: 'cover', backgroundBlendMode: 'multiply',
        }}
      >
        <Box
          styleSheet={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexDirection: {
              xs: 'column',
              sm: 'row',
            },
            width: '100%', maxWidth: '700px',
            borderRadius: '5px', padding: '32px', margin: '16px',
            boxShadow: '0 2px 10px 0 rgb(0 0 0 / 20%)',
            backgroundColor: appConfig.theme.colors.neutrals[700],
          }}
        >
          {/* Formulário */}
          <Box
            as="form"
            onSubmit={function (event) {
              event.preventDefault();
              // console.log(event);
              // window.location.href = '/chat'; é uma forma de direcionar quando fizer o submit
              // roteamento.push('/chat);
              roteamento.push(`/chat?userName=${username}`);
            }}
            styleSheet={{
              display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
              width: { xs: '100%', sm: '50%' }, textAlign: 'center', marginBottom: '32px',
            }}
          >
            <Title tag="h2">Boas vindas de volta!</Title>
            <Text variant="body3" styleSheet={{ marginBottom: '32px', color: appConfig.theme.colors.neutrals[300] }}>
              {appConfig.name}
            </Text>

            {/* <input 
              type="text"
              value={userName}
              onChange={function (event){
                console.log('Digitado: ', event.target.value);
                // Onde está o valor novo?
                const valor = event.target.value;
                // Trocar o valor da variável usando o React
                setUserName(valor);
              }}
            />  */}
            <TextField
              value={username}
              placeholder="Digite um nome de usuário válido!"
              onChange={handleChangeUsername}
              fullWidth
              textFieldColors={{
                neutral: {
                  textColor: appConfig.theme.colors.neutrals[200],
                  mainColor: appConfig.theme.colors.neutrals[900],
                  mainColorHighlight: appConfig.theme.colors.primary[500],
                  backgroundColor: appConfig.theme.colors.neutrals[800],
                },
              }}
            />
            <Button
              type='submit'
              label='Entrar'
              fullWidth
              buttonColors={{
                contrastColor: appConfig.theme.colors.neutrals["000"],
                mainColor: appConfig.theme.colors.primary[500],
                mainColorLight: appConfig.theme.colors.primary[400],
                mainColorStrong: appConfig.theme.colors.primary[600],
              }}
            />
          </Box>
          {/* Formulário */}


          {/* Photo Area */}
          <Box
            styleSheet={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              maxWidth: '200px',
              padding: '16px',
              backgroundColor: appConfig.theme.colors.neutrals[800],
              border: '1px solid',
              borderColor: appConfig.theme.colors.neutrals[999],
              borderRadius: '10px',
              flex: 1,
              minHeight: '240px',
            }}
          >
            <Image
              styleSheet={{
                borderRadius: '50%',
                marginBottom: '16px',
              }}
              src={username.length >= 3 ? `https://github.com/${username}.png` : undefined}
              alt={username.length >= 3 ? `Imagem do usuário ${username}` : ''}
            />
            <Text
              variant="body4"
              styleSheet={{
                color: appConfig.theme.colors.neutrals[200],
                backgroundColor: appConfig.theme.colors.neutrals[900],
                padding: '3px 10px',
                borderRadius: '1000px',
                textAlign: 'center',
              }}
            >
              {username.length <= 2 ? 'Informe um nome de usuário' : username + (location ? ' - ' + location : '') + (followers ? ' Followers = ' + followers : '')}
            </Text>
          </Box>
          {/* Photo Area */}
        </Box>
      </Box>
    </>
  );
}
