// OPE Utilities
// Copyright (C) 2020-2023  Motagamwala Taha Arif Ali

// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.
const crypto = require('crypto')
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const key = crypto.createSecretKey(crypto.randomBytes(32)).export({ format: "jwk" })

console.log("The key is generated copy it and paste it in your server env file or secrets area")

console.log(JSON.stringify(key))

const rl = readline.createInterface({ input, output });

rl.question('Press any key to exit', (key) => {
    rl.close();
});
