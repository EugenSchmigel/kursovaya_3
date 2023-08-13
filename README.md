The algorithm prepare on the backend data to be displayed in the cosole a list of the last 5 operations in the format:

<date> <description>
<from where> -> <to>
<amount> <currency>


For each transaction there is the following data:

- `id` - transaction id
- `date` - information about the date of the transaction
- `state` - transfer status
    - `EXECUTED` - executed,
    - `CANCELED` - cancelled.
- `operationAmount` - operation amount and currency
- `description` - description of transfer type
- `from` - from where
- `to` - where to


REQUIRMENT:

- The last 5 executed (EXECUTED) operations are displayed on the screen.
- The operations are separated by an empty line.
- The date of transfer is presented in the format DD.MM.YYYY (example: 14.10.2018).
- At the top of the list are the most recent transactions (ordered by date).
- The card number is masked and is not displayed in its entirety in the format XXXX XX** **** XXXX.
- The account number is masked and is not displayed in its entirety in the format **XXXXXX.
