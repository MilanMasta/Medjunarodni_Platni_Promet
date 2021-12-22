import React, { useState, useEffect } from "react";
import {
  Box,
  Button,
  TabList,
  Tabs,
  Tab,
  TabPanel,
  Stack,
  useColorMode,
  Center,
  Alert,
  Input,
  Select,
  Text,
  FormControl,
  RadioGroup,
  InputGroup,
  Radio,
  InputLeftElement,
  Icon,
  AlertIcon,
} from "@chakra-ui/react";
import { LockIcon, AtSignIcon, ArrowRightIcon } from "@chakra-ui/icons";

import { getTransactions, makeTransaction } from "./Services/userService";
const TransactionMenu = () => {
  const { colorMode } = useColorMode();
  const [person, setPerson] = useState(
    JSON.parse(localStorage.getItem("user"))
  );
  const [error, setError] = useState("");
  const [transaction, setTransaction] = useState({
    amount: "",
    reciever: "",
    destination: "",
    id: person.id,
  });
  const [transactions, setTransactions] = useState([]);
  //   useEffect(() => {
  // setPerson(JSON.parse(localStorage.getItem("user")));
  //   }, []);

  useEffect(() => {
    console.log(person);
    console.log("poziv");
    getTransactions(person)
      .then((item) => {
        console.log(item);
        setTransactions(item);
      })
      .then(() => {
        console.log(transactions);
        // setPerson(window.localStorage.getItem("user"));
        // window.location.reload();
      });
  }, [person]);

  const handleChange = (e) => {
    const name = e.target.name; //atribut u tagu, da li je to email, godine ili ime
    const value = e.target.value;

    setTransaction({ ...transaction, [name]: value }); //person su prazna polja ukoliko nije nista proslijedjeno na unosu
    console.log(transaction);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (
      transaction.amount === "" ||
      transaction.destination === "" ||
      transaction.reciever === ""
    ) {
      setError("Unesite sva polja potrebna za transakciju.");
    } else if (person.balances["RSD"] - parseInt(transaction.amount) < 0) {
      setError("Nemate dovoljno novca na online racunu.");
    } else {
      console.log("else");
      makeTransaction(transaction)
        .then((item) => {
          if (item !== "Transaction failed.") {
            window.localStorage.setItem("user", JSON.stringify(item));
            setError("");
          } else {
            setError(item);
            alert(item);
          }
        })
        .then(() => {
          if (error !== "Transaction failed.") {
            alert("Transakcija uspjesna.");
            setPerson(window.localStorage.getItem("user"));
            window.location.reload();
          }
        });
    }
    console.log(transaction);
  };
  return (
    <Stack variant="filled" direction="column">
      <Box
        margin={4}
        border="1px"
        padding={2}
        borderRadius="lg"
        borderColor="gray.300"
        alignItems="center"
      >
        <FormControl isRequired>
          <Text>Kolicina novca:</Text>
          <InputGroup>
            <InputLeftElement children={<Icon as={ArrowRightIcon} />} />
            <Input
              type="number"
              name="amount"
              id="amount"
              value={transaction.amount}
              onChange={handleChange}
              placeholder="RSD"
              variant="filled"
              textColor="black"
            />
          </InputGroup>
          <br />
          <RadioGroup>
            <Text>Uplata na:</Text>
            <Stack direction="row" onClick={handleChange}>
              <Radio name="destination" value="banka">
                Banka
              </Radio>
              <Radio name="destination" value="onlineaccount">
                On-line account
              </Radio>
            </Stack>
          </RadioGroup>
          <br />
          <Text>Kome:</Text>
          <InputGroup>
            <InputLeftElement children={<Icon as={ArrowRightIcon} />} />
            <Input
              type="name"
              name="reciever"
              id="reciever"
              value={transaction.reciever}
              onChange={handleChange}
              placeholder="Email / Broj racuna"
              variant="filled"
              textColor="black"
            />
          </InputGroup>
        </FormControl>
        <br />
        <Button
          width="100%"
          textColor="black"
          colorScheme="yellow"
          type="submit"
          margin={2}
          padding={3}
          onClick={handleSubmit}
        >
          Izvrsi transakciju
        </Button>
        <br />
        <Center>
          {error && (
            <Alert status="error">
              <AlertIcon />
              {error}
            </Alert>
          )}
        </Center>
      </Box>
      <Box
        margin={4}
        border="1px"
        padding={2}
        borderRadius="lg"
        borderColor="gray.300"
      >
        <Select fontSize={20} bg="yellow" spacing={3}>
          <option>Transakcije</option>
          {transactions.map((cur) => {
            return (
              <option key={cur.id} value={cur.id}>
                {cur.sender.toString() +
                  " je izvrsio uplatu ka racunu " +
                  cur.reciever.toString() +
                  " u iznosu od " +
                  cur.amount.toString() +
                  " RSD."}
              </option>
            );
          })}
        </Select>
      </Box>
    </Stack>
  );
};

export default TransactionMenu;
