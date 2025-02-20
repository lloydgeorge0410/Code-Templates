import bodyParser from "body-parser";
import cors from "cors";
import express, { Express } from "express";

import router from "./routes";

const app: Express = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use("/", router);

export default app;
