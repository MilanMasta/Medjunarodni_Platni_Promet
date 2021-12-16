import React, { useState, useEffect } from "react";
import { accountVerification, depositOnAccount } from "./Services/userService";
import {
  Button,
  Stack,
  FormControl,
  InputGroup,
  InputLeftElement,
  Icon,
  Input,
  Divider,
  Alert,
  AlertIcon,
  Center,
  Text,
  Box,
  InputRightAddon,
  Stat,
  StatLabel,
  StatNumber,
  StatHelpText,
  Select,
} from "@chakra-ui/react";
import {
  EmailIcon,
  InfoIcon,
  PhoneIcon,
  LockIcon,
  WarningIcon,
  AtSignIcon,
} from "@chakra-ui/icons";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

const URL =
  "http://api.exchangeratesapi.io/v1/latest?access_key=57d102e76d357aaaab5dba8955ffa5a8";
const OnlineAccount = () => {
  const [person, setPerson] = useState(
    JSON.parse(localStorage.getItem("user"))
  );
  const [payment, setPayment] = useState({
    amount: "",
    rsdBalance: "",
    email: "",
  });

  const [array, setArray] = useState([]);
  const [currency, setCurrency] = useState([]);
  const [error, setError] = useState("");
  const [creditCard, setcreditCard] = useState({
    number: "",
    username: "",
    expirationDate: "",
    csc: "",
    balance: 0,
  });

  useEffect(() => {
    setPerson(JSON.parse(localStorage.getItem("user")));
    fetch(URL)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        //setBaseCurrency(data.base);
        setCurrency(data.rates);
        setArray([data.base, ...Object.keys(data.rates)]);
      });
  }, []);

  useEffect(() => {
    var rsdbal = person.onlineAccount.balances["RSD"];
    setPayment({ amount: "", rsdBalance: rsdbal, email: person.email });
  }, [person]);
  const handleChange = (e) => {
    const name = e.target.name; //atribut u tagu, da li je to email, godine ili ime
    const value = e.target.value;
    setcreditCard({ ...creditCard, [name]: value }); //person su prazna polja ukoliko nije nista proslijedjeno na unosu
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    if (creditCard.number && creditCard.csc) {
      accountVerification(creditCard)
        .then((item) => {
          if (item !== "Verification failed.") {
            window.localStorage.setItem("user", JSON.stringify(item));
            setError("");
          } else {
            setError(item);
          }
        })
        .then(() => {
          setPerson(window.localStorage.getItem("user"));
          window.location.reload();
        });
    } else {
      setError("Unesite sve podatke za verifikaciu.");
    }
  };

  const handleChange2 = (e) => {
    const name = e.target.name; //atribut u tagu, da li je to email, godine ili ime
    const value = e.target.value;
    setPayment({ ...payment, [name]: value }); //person su prazna polja ukoliko nije nista proslijedjeno na unosu
    console.log("val" + payment.amount);
  };
  const handleSubmit2 = (e) => {
    e.preventDefault();

    console.log(payment);
    if (payment.amount) {
      if (payment.amount >= 1) {
        console.log(array);
        // depositOnAccount(payment)
        //   .then((item) => {
        //     if (item !== "Deposit failed.") {
        //       window.localStorage.setItem("user", JSON.stringify(item));
        //       setError("");
        //     } else {
        //       setError(item);
        //     }
        //   })
        //   .then(() => {
        //     setPerson(window.localStorage.getItem("user"));
        //     window.location.reload();
        //   });
      } else {
        setError("Unesite kolicinu za uplatu vecu od 0.");
      }
    } else {
      setError("Unesite kolicinu za uplatu sa kartice.");
    }
  };

  return (
    <Box
      margin={4}
      border="1px"
      padding={2}
      borderRadius="lg"
      borderColor="gray.300"
    >
      <Stack direction="row" border={1}>
        <Stack spacing={3}>
          {person && person.verified && (
            <Stack direction="row">
              <Stack direction="column">
                <Select size="xs" placeholder="From:" name="currency">
                  {array.map((cur) => {
                    return (
                      <option key={cur} value={cur}>
                        {cur}
                      </option>
                    );
                  })}
                </Select>
                <Select size="xs" placeholder="To:" name="currency">
                  {array.map((cur) => {
                    return (
                      <option key={cur} value={cur}>
                        {cur}
                      </option>
                    );
                  })}
                </Select>
              </Stack>
              <Stack direction="column">
                <>
                  <Button
                    textColor="gray.200"
                    colorScheme="green"
                    textColor="black"
                    margin={1}
                  >
                    Verifikovan
                  </Button>
                  <form action="submit">
                    <FormControl isRequired>
                      <Text fontSize="sm">Kolicina za uplatu:</Text>
                      <InputGroup>
                        <InputLeftElement children={<Icon as={InfoIcon} />} />
                        <Input
                          type="number"
                          name="amount"
                          id="amount"
                          value={payment.amount}
                          onChange={handleChange2}
                          placeholder="Kolicina"
                          variant="filled"
                          textColor="black"
                        />
                        <InputRightAddon children="RSD" />
                      </InputGroup>
                    </FormControl>
                    <br />
                    <Stat>
                      <StatLabel>Trenutno stanje on-line racuna</StatLabel>
                      <StatNumber>{payment.rsdBalance}</StatNumber>
                      <StatHelpText>RSD</StatHelpText>
                    </Stat>
                    <br />
                    <Divider />
                    <br />
                    <Button
                      width="100%"
                      textColor="black"
                      colorScheme="yellow"
                      type="submit"
                      onClick={handleSubmit2}
                    >
                      Uplati na racun
                    </Button>
                  </form>
                </>
              </Stack>
            </Stack>
          )}
          {person && !person.verified && (
            <>
              <Button
                textColor="gray.200"
                colorScheme="green"
                textColor="black"
                margin={1}
              >
                Nalog nije verifikovan
              </Button>
            </>
          )}
          {person && !person.verified && (
            <form action="submit">
              <FormControl isRequired>
                <Text fontSize="sm">Broj platne kartice:</Text>
                <InputGroup>
                  <InputLeftElement children={<Icon as={InfoIcon} />} />
                  <Input
                    type="number"
                    name="number"
                    id="number"
                    value={creditCard.number}
                    onChange={handleChange}
                    placeholder="Broj kartice"
                    variant="filled"
                    textColor="black"
                  />
                </InputGroup>
              </FormControl>
              <FormControl isRequired>
                <Text fontSize="sm">Sigurnosni kod:</Text>
                <InputGroup>
                  <InputLeftElement children={<Icon as={InfoIcon} />} />
                  <Input
                    type="name"
                    name="csc"
                    id="csc"
                    value={creditCard.csc}
                    onChange={handleChange}
                    placeholder="Sigurnosni kod"
                    variant="filled"
                    textColor="black"
                  />
                </InputGroup>
              </FormControl>
              <br />
              <Divider />
              <br />
              <Button width="100%" type="submit" onClick={handleSubmit}>
                Verifikuj
              </Button>
            </form>
          )}
          <Center>
            {error && (
              <Alert status="error">
                <AlertIcon />
                {error}
              </Alert>
            )}
          </Center>
        </Stack>
      </Stack>
    </Box>
  );
};

export default OnlineAccount;
