"""                     Aula 2
Quando  se coloca um input, com value no react, ele para de funcionar. Isso porque o valor ser algo que muda, mas o react não sabe reagir a isso, com isso vem a necessidade da função "onchange", mas ainda sim não há mudança
Ex: 
        {/* <input 
              type="text"
              value={userName}
              onChange={function (event){          //Sempre quando é digitado ele devolve a infodeeventos
              console.log('Digitado: ', event.target.value);     //Não precisa estar entre {} pois é           
                // Onde está o valor novo?                        //um elemento JS puro
                const valor = event.target.value;
                // Trocar o valor da variável usando o React
                setUserName(valor);
              }}
            />  */}

# Quando se digita, abre ou modifica na página, é uma alteração de estado no React, para que haja a alteração do elemento usa-se:
const [username, setUserName] = React.useState('RafaelAndradeDev'); //React.useState é uma função que retorno 
                                                        //um array, que o primeiro valor é vazio, o segundo é
                                                        //uma função que modifica o valor
Logo após faça a alteração dessa variável de mudança:
setUserName(valor);        //Ele comunica ao react qual variável precisa mudar na página

Dessa forma a cada digitação no espaço do input, todos os locais cujo a variável foi chamada é alterada. Isso porque o React é rápido em modificar, por seu sistema de alterações que são enviadas de uma vez, não de cada uma

# O padrão de um formulário é sempre fazer um refresh na página  //as="form"
Sempre que há uma tag de formulário pode ser passado um valor "onSubmit":

onSubmit={function (event) {
              event.preventDefault();  //Para evitar que a página seja recarregada quando for feito o submit
              }}

# Existe um push dentro dos eventos, que é para adicionar mais uma URL dentro da aplicação, sem fazer o navegador processar muito.

Primeiramente declara 
const roteamento = useRouter();             //Através da manipulação dele podemos modificar a página
//window.location.href = '/chat'; é uma forma de direcionar quando fizer o submit (FORMA LENTA)
//roteamento.push('/chat);


# O Next possui um arquivo que possui todas as páginas que vão ser carregadas, se quiser que algo fique em volta de tudo, como um style, basta colocar nele. Tudo fica nessa documentação:
*https://nextjs.org/docs/advanced-features/custom-app         //É algo já reconhecido pelo Next 










 """
