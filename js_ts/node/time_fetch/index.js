#! /usr/bin/env node 

import { JSDOM } from 'jsdom';

const MYURL = 'https://www.worldtimeserver.com/current_time_in_GB.aspx';
const RESULT = await (await fetch(MYURL)).text();
const { document } = (new JSDOM(RESULT)).window;

console.log(document.querySelector('#myTime').textContent.trim());
